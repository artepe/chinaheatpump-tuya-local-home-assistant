import base64
import copy
import json
import struct
import threading
import traceback
from pathlib import Path

import pytest

from custom_components.mango_tuya_local.client import MangoClient, MangoWriteError
from custom_components.mango_tuya_local.protocol import (
    Headers,
    MangoError,
    MangoProfileError,
    MangoReadError,
    MangoValueError,
    Profile,
    common_temperatures,
    write_frame,
)

from .fake_device import Hardware


@pytest.fixture
def profile():
    return Profile.load()


@pytest.fixture
def pair(profile):
    hardware = Hardware(profile)
    counter = iter(range(1, 50000))
    client = MangoClient(
        "127.0.0.1",
        "TEST_DEVICE",
        "0000000000000000",
        profile,
        device_factory=hardware.factory,
        clock=lambda: 0,
        pause=lambda n: None,
        header_factory=lambda size: next(counter).to_bytes(size, "big"),
    )
    return client, hardware


def test_all_770_actual_routes_and_no_34_backups(profile, pair):
    client, hardware = pair
    snapshots = [client.read_group(g) for g in range(17)]
    assert sum(len(s.fields) for s in snapshots) == 770
    assert len(snapshots[14].fields) == 46
    assert len(snapshots[16].fields) == 14
    for slot in (14, 20, 47):
        with pytest.raises(MangoProfileError):
            profile.parameter(16, slot)
    assert hardware.writes == 0
    assert len({raw[1:4] for raw in hardware.sent}) == len(hardware.sent)


def test_four_observed_owner_write_frames_match_byte_for_byte(profile, pair):
    client, _ = pair
    fixture = json.loads(
        Path(__file__).with_name("fixtures").joinpath("observed_write_frames.json").read_text()
    )
    for observed in fixture["frames"]:
        p = profile.parameter(observed["group"], observed["slot"])
        field = client.read_group(p.group).field(p)
        actual = write_frame(bytes.fromhex(observed["header_hex"]), p, field, observed["raw_value"])
        assert actual == base64.b64decode(observed["value_b64"], validate=True)


@pytest.mark.parametrize("key,target", [("14:16", 31), ("1:10", 0), ("0:20", 1), ("2:0", 1)])
def test_one_chosen_parameter_is_written_and_freshly_confirmed(key, target, pair):
    client, hardware = pair
    group, slot = map(int, key.split(":"))
    p = client.profile.parameter(group, slot)
    if key == "2:0":
        target = min(p.upper, max(p.lower, hardware.values[key] + 1))
    result = client.set_raw(p, target)
    assert result.changed and result.snapshot.field(p).value == target
    assert hardware.values[key] == target and hardware.writes == 1
    assert client.last_operation["write_verified"]
    assert len({raw[1:4] for raw in hardware.sent}) == len(hardware.sent)


def test_same_value_never_sends_a_parameter_write(pair):
    client, hardware = pair
    result = client.set_raw(client.profile.parameter(14, 16), 30)
    assert not result.changed and hardware.writes == 0
    assert not client.last_operation["write_verified"]


@pytest.mark.parametrize("value", [101, -101, 32768, -32769, True, 0.1, "1"])
def test_values_are_checked_against_fresh_bounds(value, pair):
    client, hardware = pair
    with pytest.raises(MangoValueError):
        client.set_raw(client.profile.parameter(1, 10), value)
    assert hardware.writes == 0


def test_changed_device_bounds_block_write(pair):
    client, hardware = pair
    hardware.plans[1] = "narrow_bounds"
    with pytest.raises(MangoValueError):
        client.set_raw(client.profile.parameter(1, 10), -1)
    assert hardware.writes == 0


def test_simulated_negative_value_is_signed16_without_claiming_live_acceptance(pair):
    client, hardware = pair
    client.set_raw(client.profile.parameter(1, 10), -1)
    assert next(raw for raw in hardware.sent if raw[4] == 4)[9:11] == b"\xff\xff"
    assert hardware.values["1:10"] == -1


@pytest.mark.parametrize("action", ["missing", "wrong_header", "wrong_id", "wrong_padding"])
def test_missing_or_wrong_pre_write_reply_never_writes(action, pair):
    client, hardware = pair
    hardware.plans = {n: action for n in (1, 2, 3)}
    with pytest.raises(MangoReadError):
        client.set_raw(client.profile.parameter(14, 16), 31)
    assert hardware.writes == 0


@pytest.mark.parametrize("action", ["missing", "stale", "changed_metadata"])
def test_bad_post_write_reply_restores_original(action, pair):
    client, hardware = pair
    hardware.plans = {2: action, 3: action}
    with pytest.raises(MangoWriteError) as result:
        client.set_raw(client.profile.parameter(14, 16), 31)
    assert result.value.restored and hardware.values["14:16"] == 30
    assert not client.last_operation["write_verified"]


def test_delayed_value_retries_read_without_resending_target(pair):
    client, hardware = pair
    hardware.plans[2] = "stale"
    client.set_raw(client.profile.parameter(14, 16), 31)
    assert hardware.writes == 1 and hardware.reads == 3


def test_send_error_after_possible_delivery_restores_and_does_not_leak_payload(pair):
    client, hardware = pair
    hardware.fail_send = True
    with pytest.raises(MangoWriteError) as result:
        client.set_raw(client.profile.parameter(14, 16), 31)
    assert result.value.restored and hardware.values["14:16"] == 30
    assert "PRIVATE_TRANSPORT_PAYLOAD" not in "".join(traceback.format_exception(result.value))


def test_cancel_after_send_restores_before_worker_returns(pair):
    client, hardware = pair
    abort = threading.Event()
    hardware.abort_after_send = abort
    with pytest.raises(MangoWriteError) as result:
        client.set_raw(client.profile.parameter(14, 16), 31, abort)
    assert result.value.restored and hardware.values["14:16"] == 30


def test_failed_restore_is_bounded_and_reported(pair):
    client, hardware = pair
    hardware.ignore_restore = True
    hardware.plans = {2: "missing", 3: "missing"}
    with pytest.raises(MangoWriteError) as result:
        client.set_raw(client.profile.parameter(14, 16), 31)
    assert not result.value.restored and hardware.writes == 3
    assert result.value.original == 30


def test_rejected_target_is_not_marked_verified(pair):
    client, hardware = pair
    hardware.ignore_target = True
    with pytest.raises(MangoWriteError) as result:
        client.set_raw(client.profile.parameter(14, 16), 31)
    assert result.value.restored and not client.verified_writes


def test_known_scale_metadata_change_blocks_write(pair):
    client, hardware = pair
    hardware.plans[1] = "changed_metadata"
    with pytest.raises(MangoProfileError):
        client.set_raw(client.profile.parameter(1, 10), 0)
    assert hardware.writes == 0


def test_private_dp102_is_not_retained(pair):
    client, hardware = pair
    hardware.private_status = True
    client.status()
    client.read_group(1)
    assert not client.temperatures
    assert "PRIVATE_VALUE" not in repr(client.__dict__)


def test_profile_validation_only_reads_anchors(pair):
    client, hardware = pair
    client.validate_profile()
    assert hardware.reads == 2 and hardware.writes == 0


def test_decimal_conversion_only_for_confirmed_scale(profile):
    p = profile.parameter(1, 10)
    assert p.to_raw(0.1) == 1 and p.to_raw(-0.1) == -1
    with pytest.raises(MangoValueError):
        p.to_raw(0.15)
    with pytest.raises(MangoValueError):
        profile.parameter(14, 16).to_raw(30.1)
    assert sum(p.scale_verified for p in profile.parameters.values()) == 1


def test_stale_dp16_and_missing_temperature_do_not_become_zero():
    assert common_temperatures({"16": 63}) == {}
    raw = bytearray(244)
    raw[:6] = bytes.fromhex("010100010001")
    struct.pack_into(">hhh", raw, 14, 63, 75, 18)
    struct.pack_into(">h", raw, 92, 627)
    assert common_temperatures({"105": base64.b64encode(raw).decode()}) == {
        "target_temperature": 63.0,
        "current_temperature": 62.7,
    }
    struct.pack_into(">h", raw, 92, -32700)
    assert "current_temperature" not in common_temperatures({"105": base64.b64encode(raw).decode()})


def test_profile_rejects_duplicate_and_backup_routes():
    data = json.loads(
        Path(__file__).parents[1].joinpath("custom_components/mango_tuya_local/profile.json").read_text()
    )
    bad = copy.deepcopy(data)
    bad["routes"].append(bad["routes"][0])
    with pytest.raises(MangoProfileError):
        Profile(bad)


def test_header_memory_is_bounded_and_rejects_recent_reuse():
    seq = iter(range(1, 5000))
    headers = Headers(lambda n: next(seq).to_bytes(n, "big"))
    for _ in range(4100):
        headers.new()
    assert len(headers.used) == len(headers.recent) == 4096
    headers.factory = lambda n: (4100).to_bytes(n, "big")
    with pytest.raises(MangoError):
        headers.new()
