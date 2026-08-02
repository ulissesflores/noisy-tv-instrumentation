"""Build (or verify) the SHA-256 provenance chain of this repository.

The chain covers what the scientific claim depends on — code, tests, declared
data and derived results — and deliberately excludes what varies per machine
(platform, interpreter version, rendered figures). One ``chain_hash`` seals
the set: if any hashed byte changes, the hash changes.

Usage
-----
``python make_provenance.py``            build ``output/provenance.json`` + ``output/hash-chain.md``
``python make_provenance.py --verify``   recompute and compare against the stored chain
"""

import hashlib
import json
import platform
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent

HASHED_GLOBS = [
    "code/*.py",
    "code/requirements.txt",
    "tests/*.py",
    "data/*.json",
    "data/*.md",
    "output/results.json",
]
"""What the claim depends on. Figures and lockfiles are informational only."""


def sha256_file(path: Path) -> str:
    """Return the hex SHA-256 digest of a file's bytes.

    Parameters
    ----------
    path : Path
        File to hash.

    Returns
    -------
    str
        64-character hexadecimal digest.
    """
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build_manifest() -> dict:
    """Hash every covered file and derive the single chain hash.

    Returns
    -------
    dict
        ``{"files": {relpath: sha256}, "chain_hash": str}`` with paths sorted
        so the chain is order-independent and reproducible anywhere.
    """
    files: dict[str, str] = {}
    for pattern in HASHED_GLOBS:
        for path in sorted(ROOT.glob(pattern)):
            files[path.relative_to(ROOT).as_posix()] = sha256_file(path)
    concat = "".join(f"{name}:{digest}\n" for name, digest in sorted(files.items()))
    return {"files": files, "chain_hash": hashlib.sha256(concat.encode()).hexdigest()}


def write_outputs(manifest: dict) -> None:
    """Write ``provenance.json`` and the human-readable ``hash-chain.md``.

    Parameters
    ----------
    manifest : dict
        Output of :func:`build_manifest`.
    """
    out = ROOT / "output"
    out.mkdir(exist_ok=True)
    (out / "provenance.json").write_text(json.dumps(manifest, indent=2) + "\n")
    lines = [
        "# Provenance hash chain",
        "",
        f"**chain_hash:** `{manifest['chain_hash']}`",
        "",
        "Recompute and compare with: `python make_provenance.py --verify`",
        "",
        "## Hashed (the claim depends on these bytes)",
        "",
        "| File | SHA-256 |",
        "|---|---|",
    ]
    lines += [f"| `{n}` | `{d}` |" for n, d in sorted(manifest["files"].items())]
    lines += [
        "",
        "## Informational (NOT hashed)",
        "",
        f"- Generated: {date.today().isoformat()}",
        f"- Python: {platform.python_version()} on {platform.system()} {platform.machine()}",
        "- Figures (`output/figures/`) and `requirements.lock` are excluded so the",
        "  chain survives machine and renderer changes; results are what is sealed.",
    ]
    (out / "hash-chain.md").write_text("\n".join(lines) + "\n")


def verify() -> int:
    """Recompute the chain and compare against the stored provenance.

    Returns
    -------
    int
        0 when the stored and recomputed chain hashes match, 1 otherwise.
    """
    stored_path = ROOT / "output" / "provenance.json"
    if not stored_path.exists():
        print("FAIL: output/provenance.json not found — run `python make_provenance.py` first")
        return 1
    stored = json.loads(stored_path.read_text())
    current = build_manifest()
    if stored["chain_hash"] == current["chain_hash"]:
        print(f"OK: chain_hash verified ({current['chain_hash'][:16]}…)")
        return 0
    print("FAIL: chain_hash mismatch")
    for name in sorted(set(stored["files"]) | set(current["files"])):
        if stored["files"].get(name) != current["files"].get(name):
            print(f"  changed: {name}")
    return 1


if __name__ == "__main__":
    if "--verify" in sys.argv:
        raise SystemExit(verify())
    write_outputs(build_manifest())
    print(f"chain_hash: {build_manifest()['chain_hash']}")
