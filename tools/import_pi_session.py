#!/usr/bin/env python3
"""Export only the selected pump's credentials to the local HA setup file."""

import argparse
import contextlib
import io
import json
import os
import tempfile
from pathlib import Path


def config_root(value=None):
    candidates = [Path(value)] if value else [Path("/homeassistant"), Path("/config")]
    for candidate in candidates:
        if (candidate / "configuration.yaml").is_file():
            return candidate.resolve()
    raise RuntimeError("HOME_ASSISTANT_CONFIG_KANSIOTA_EI_LOYDY")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", required=True)
    parser.add_argument("--ha-config")
    parser.add_argument("--device-name", default="Mango Energy")
    args = parser.parse_args()
    try:
        root = config_root(args.ha_config)
        import tuya_devices as td

        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            session = td.load_session(td.DEFAULT_SESSION)
            devices = td.devices_from_session(session, td.DEFAULT_SESSION) if session else []
            matches = [
                d
                for d in devices
                if getattr(d, "product_name", "") == args.device_name
                or getattr(d, "name", "") == args.device_name
            ]
            if len(matches) != 1:
                raise RuntimeError("LAITTEEN_VALINTA_EI_ONNISTUNUT")
            device = td.device_dict(matches[0])
        data = {
            "format": "mango_tuya_local_credentials_v1",
            "host": args.host,
            "device_id": device["id"],
            "local_key": device["local_key"],
        }
        if not data["device_id"] or len(data["local_key"].encode()) != 16:
            raise RuntimeError("LAITTEEN_PAIKALLISET_TUNNUKSET_EIVAT_KELPAA")
        fd, temp = tempfile.mkstemp(prefix=".mango-credentials-", dir=root)
        try:
            with os.fdopen(fd, "w") as handle:
                json.dump(data, handle)
                handle.write("\n")
                handle.flush()
                os.fsync(handle.fileno())
            os.replace(temp, root / "mango_tuya_local_credentials.json")
        finally:
            if os.path.exists(temp):
                os.unlink(temp)
        print("PAIKALLISET_TUNNUKSET_TUOTU. Niita ei tulostettu.")
        print("HA: Asetukset > Laitteet ja palvelut > Lisaa integraatio > Mango Tuya Local")
        print("Valitse: Kayta Pi:n istunnosta tuotuja tunnuksia.")
        return 0
    except Exception as error:
        print("TUONTI_EI_ONNISTUNUT:", type(error).__name__)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
