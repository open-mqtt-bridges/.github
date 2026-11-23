"""Validate shared organization defaults, profile consistency and Spec Kit assets."""
from pathlib import Path
import re
import subprocess

root = Path(__file__).resolve().parents[1]
required = ["LICENSE", "CONTRIBUTING.md", "SECURITY.md", "CODE_OF_CONDUCT.md", ".github/PULL_REQUEST_TEMPLATE.md", ".github/ISSUE_TEMPLATE/bug_report.yml", ".github/ISSUE_TEMPLATE/feature_request.yml", "assets/logo.svg", "assets/logo.png", "assets/favicon.svg"]
for name in required:
    assert (root / name).is_file(), f"Missing organization file: {name}"
region = re.compile(r"<!-- bridges:start -->\n([\s\S]*?)\n<!-- bridges:end -->")
tables = [region.search((root / name).read_text()).group(1) for name in ["README.md", "profile/README.md"]]
assert tables[0] == tables[1], "README and profile bridge tables differ"
expected = ["adguardhome", "display", "homeconnect", "idm-energy", "landroid", "modbus", "philips-hue", "pocketbase", "roborock", "wled"]
source_base = "https://github.com/open-mqtt-bridges/open-mqtt-bridges.github.io/tree/main"
rows = [row for row in tables[0].splitlines() if row.startswith("| [")]
assert len(rows) == len(expected), "Expected exactly ten bridge entries"
assert tables[0].count("| Archived |") == 1
for slug, row in zip(expected, rows):
    directory = "archive" if slug == "idm-energy" else "bridges"
    source = re.match(r"^\| \[[^\]]+\]\(([^)]+)\) \|", row)
    assert source and source[1] == f"{source_base}/{directory}/{slug}", f"Incorrect source or order: {slug}"
    if slug in ["adguardhome", "idm-energy"]:
        assert f"[README](https://github.com/open-mqtt-bridges/{slug}#readme)" in row
    else:
        assert f"[Docs](https://open-mqtt-bridges.github.io/{slug}/)" in row
    assert row.endswith("| Archived |" if slug == "idm-energy" else "| Active |"), f"Incorrect status: {slug}"
assert len(list((root / ".agents/skills").glob("speckit-*/SKILL.md"))) == 9
for script in (root / ".specify/scripts/bash").glob("*.sh"):
    subprocess.run(["bash", "-n", str(script)], check=True)
print("Shared community files, matching sorted bridge lists, branding and Spec Kit passed.")
