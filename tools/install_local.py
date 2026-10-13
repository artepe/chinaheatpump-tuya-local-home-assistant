#!/usr/bin/env python3
"""Install this checkout without restarting HA or writing device parameters."""

import argparse
import datetime
import json
import os
import shutil
import tempfile
from pathlib import Path

from import_pi_session import config_root


def install(source: Path, config: Path) -> Path:
    manifest = json.loads((source / "manifest.json").read_text())
    if manifest["domain"] != "mango_tuya_local":
        raise ValueError("INTEGRAATION_TUNNISTE_EI_KELPAA")
    components = config / "custom_components"
    components.mkdir(exist_ok=True)
    destination = components / "mango_tuya_local"
    stage_parent = Path(tempfile.mkdtemp(prefix=".mango-install-", dir=config))
    staged = stage_parent / "mango_tuya_local"
    backup = None
    try:
        shutil.copytree(source, staged, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        if destination.exists():
            backup_root = config / "mango_tuya_local_backups"
            backup_root.mkdir(exist_ok=True)
            stamp = datetime.datetime.now(datetime.UTC).strftime("%Y%m%dT%H%M%S%fZ")
            backup = backup_root / stamp
            os.replace(destination, backup)
        try:
            os.replace(staged, destination)
        except BaseException:
            if backup is not None:
                os.replace(backup, destination)
            raise
        return destination
    finally:
        shutil.rmtree(stage_parent)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ha-config")
    args = parser.parse_args()
    try:
        config = config_root(args.ha_config)
        source = Path(__file__).resolve().parents[1] / "custom_components" / "mango_tuya_local"
        destination = install(source, config)
        print("INTEGRAATIO_ASENNETTU:", destination)
        print("KAYNNISTA_HOME_ASSISTANT_UUDELLEEN: ha core restart")
        print("Lisaa sitten Mango Tuya Local laitteet ja palvelut -sivulta.")
        return 0
    except Exception as error:
        print("ASENNUS_EI_ONNISTUNUT:", type(error).__name__)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
