#!/usr/bin/env python3
"""Exercise the documented SDK download block with benign local fixtures."""

import bz2
import hashlib
import io
import os
from pathlib import Path
import subprocess
import tarfile
import tempfile


ROOT = Path(__file__).resolve().parents[1]
PAGES = (
    ROOT / "docs/en/software/board/sdk-download.md",
    ROOT / "docs/zh_CN/software/board/sdk-download.md",
)
START = "<!-- sdk-download-example:start -->"
END = "<!-- sdk-download-example:end -->"
PUBLISHED = {
    "anykavision-km02g-sdk-1.00.tar.gz": "6e269573adc50dd2ed11e3bc6f22bd0dca481bde2b58c1794bcbdf6fad9a4b22",
    "busybox-1.35.0.tar.bz2": "faeeb244c35a348a334f4a59e44626ee870fb07b6884d68c10ae8bc19f83a694",
    "mtd-utils-2.3.1.tar.bz2": "03d9dc58ad10ea3549d9528f6b17a44d8944e18e96c0f31474f9f977078b83dc",
}


def extract(page):
    text = page.read_text(encoding="utf-8")
    assert text.count(START) == text.count(END) == 1, f"missing example markers in {page}"
    fenced = text.split(START, 1)[1].split(END, 1)[0].strip().splitlines()
    assert fenced[0] == "```bash" and fenced[-1] == "```", f"bad example fence in {page}"
    return "\n".join(fenced[1:-1]) + "\n"


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def make_fixture(directory):
    sdk = directory / "anykavision-km02g-sdk-1.00.tar.gz"
    with tarfile.open(sdk, "w:gz") as archive:
        data = b"benign SDK fixture\n"
        info = tarfile.TarInfo("anykavision-km02g-sdk-1.00/README.fixture")
        info.size = len(data)
        archive.addfile(info, io.BytesIO(data))
        tools = tarfile.TarInfo("anykavision-km02g-sdk-1.00/tools")
        tools.type = tarfile.DIRTYPE
        tools.mode = 0o755
        archive.addfile(tools)
    (directory / "busybox-1.35.0.tar.bz2").write_bytes(bz2.compress(b"benign BusyBox fixture\n"))
    (directory / "mtd-utils-2.3.1.tar.bz2").write_bytes(bz2.compress(b"benign mtd fixture\n"))
    checksums = "".join(f"{sha256(directory / name)}  {name}\n" for name in PUBLISHED)
    (directory / "SHA256SUMS").write_text(checksums, encoding="ascii")


def run_case(script, name, *, missing_entry=None, fail_asset=None, corrupt_asset=None, succeeds=False):
    with tempfile.TemporaryDirectory(prefix=f"sdk-download-{name}-") as temp:
        temp = Path(temp)
        fixture, download, fakebin = temp / "fixture", temp / "download", temp / "bin"
        fixture.mkdir()
        download.mkdir()
        fakebin.mkdir()
        make_fixture(fixture)
        if missing_entry:
            manifest = (fixture / "SHA256SUMS").read_text(encoding="ascii")
            (fixture / "SHA256SUMS").write_text(
                "".join(line for line in manifest.splitlines(keepends=True) if not line.endswith(f"  {missing_entry}\n")),
                encoding="ascii",
            )
        curl = fakebin / "curl"
        curl.write_text(
            "#!/usr/bin/env bash\n"
            "set -eu\n"
            "url=${!#}\n"
            "asset=${url##*/}\n"
            "test \"$asset\" != \"${FAIL_ASSET:-}\" || exit 22\n"
            "cp \"$FIXTURE_DIR/$asset\" \"$asset\"\n"
            "test \"$asset\" != \"${CORRUPT_ASSET:-}\" || printf x >> \"$asset\"\n",
            encoding="ascii",
        )
        curl.chmod(0o755)
        fixture_hashes = {asset: sha256(fixture / asset) for asset in PUBLISHED}
        case_script = script
        for asset, published_hash in PUBLISHED.items():
            case_script = case_script.replace(published_hash, fixture_hashes[asset])
        env = os.environ | {
            "PATH": f"{fakebin}{os.pathsep}{os.environ['PATH']}",
            "FIXTURE_DIR": str(fixture),
            "FAIL_ASSET": fail_asset or "",
            "CORRUPT_ASSET": corrupt_asset or "",
        }
        result = subprocess.run(
            ["bash", "-c", case_script], cwd=download, env=env,
            text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        )
        extracted = download / "anykavision-km02g-sdk-1.00"
        if succeeds:
            assert result.returncode == 0, f"{name} unexpectedly failed:\n{result.stdout}"
            for asset in tuple(PUBLISHED)[1:]:
                assert (extracted / "tools" / asset).is_file(), f"{name} did not move {asset}"
        else:
            assert result.returncode != 0, f"{name} unexpectedly succeeded"
            assert not extracted.exists(), f"{name} extracted the SDK after a failed check"


english, chinese = map(extract, PAGES)
assert english == chinese, "English and Chinese download commands differ"
for asset, digest in PUBLISHED.items():
    assert f"{digest}  {asset}" in english, f"published hash missing for {asset}"

run_case(english, "success", succeeds=True)
run_case(english, "corrupt", corrupt_asset="anykavision-km02g-sdk-1.00.tar.gz")
run_case(english, "missing-manifest-entry", missing_entry="mtd-utils-2.3.1.tar.bz2")
run_case(english, "failed-download", fail_asset="busybox-1.35.0.tar.bz2")
print("SDK download example: success and three fail-closed cases passed")
