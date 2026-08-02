"""Single-entry replication: demos -> results.json -> tests -> provenance.

Run ``python run_all.py`` in a fresh clone (after ``pip install -r
code/requirements.txt``) and everything the article publishes is recomputed,
asserted and sealed. Exit code 0 means: numbers reproduced, suite green,
provenance chain built and verified.
"""

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "code"))

from gap_intensity import SIGMA_D32, ghost_gap_scenario  # noqa: E402
from noise_floor import SEED, noise_floor  # noqa: E402


def compute_results() -> dict:
    """Recompute every headline number and return them as one dict.

    Returns
    -------
    dict
        Noise floors, the ghost-gap scenario and the seed used — the exact
        numbers the article publishes, freshly derived.
    """
    gap, intensity = ghost_gap_scenario()
    return {
        "seed": SEED,
        "noise_floor": {
            "d32": round(noise_floor(32), 3),
            "d384": round(noise_floor(384), 3),
        },
        "ghost_gap": {
            "sigma_input": SIGMA_D32,
            "gap": round(gap, 3),
            "intensity": round(intensity, 2),
        },
    }


def main() -> int:
    """Run the full replication pipeline and seal the provenance chain.

    Returns
    -------
    int
        0 on full success; the exit code of the first failing stage otherwise.
    """
    results = compute_results()
    out = ROOT / "output"
    out.mkdir(exist_ok=True)
    (out / "results.json").write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
    print(f"[1/3] results.json written: {results['noise_floor']} / {results['ghost_gap']}")

    tests = subprocess.run([sys.executable, "-m", "pytest", "-q"], cwd=ROOT)
    if tests.returncode != 0:
        return tests.returncode
    print("[2/3] test suite green")

    build = subprocess.run([sys.executable, "make_provenance.py"], cwd=ROOT)
    if build.returncode != 0:
        return build.returncode
    check = subprocess.run([sys.executable, "make_provenance.py", "--verify"], cwd=ROOT)
    print("[3/3] provenance chain built and verified")
    return check.returncode


if __name__ == "__main__":
    raise SystemExit(main())
