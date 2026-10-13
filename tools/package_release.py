#!/usr/bin/env python3
"""Package only tracked source files and the reusable dashboard YAML."""

import argparse
import json
import shutil
import subprocess
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="release-assets")
    args = parser.parse_args()
    output = Path(args.output).resolve()
    output.mkdir(parents=True, exist_ok=True)
    version = json.loads((ROOT / "custom_components/mango_tuya_local/manifest.json").read_text())["version"]
    names = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT).decode().split("\0")
    target = output / f"mango-tuya-local-v{version}.zip"
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name in sorted(n for n in names if n):
            if name.endswith("_credentials.json") or name in ("session.json", "devices.json"):
                raise ValueError("private_file_in_release")
            archive.write(ROOT / name, Path("mango_tuya_home_assistant") / name)
    shutil.copyfile(ROOT / "dashboards/mango_control_room.yaml", output / "mango_control_room.yaml")
    print(target.name)


if __name__ == "__main__":
    main()
