"""Regenerate the repository figures from the declared data. No figure without a claim.

Claim map
---------
``fig1-noise-floor``
    CLAIM: the cosine noise floor follows ~1/sqrt(d) and, below d ~= 86, exceeds
    the ranking signals it is supposed to measure (0.108, 0.100). Measured
    points: sigma = 0.177 at d=32 and 0.051 at d=384 (data/measurements.json).

Requires matplotlib (not a runtime dependency): ``pip install matplotlib``.
Outputs PNG + SVG under ``output/figures/`` — informational, excluded from the
provenance chain so the seal survives renderer changes.
"""

import json
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]


def fig1_noise_floor(outdir: Path) -> None:
    """Plot the 1/sqrt(d) floor, the measured points and the drowned signals.

    Parameters
    ----------
    outdir : Path
        Directory receiving ``fig1-noise-floor.png`` and ``.svg``.
    """
    data = json.loads((ROOT / "data" / "measurements.json").read_text())
    points = [(v["dim"], v["sigma_demo"]) for v in data["cosine_noise_floor"]["values"]]
    signals = {
        v["name"]: v["value"]
        for v in data["signals_vs_noise"]["values"]
        if "noise floor" not in v["name"]
    }

    d = np.logspace(np.log10(8), np.log10(768), 200)
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.plot(d, 1 / np.sqrt(d), color="#555", lw=1.5, label="theory: 1/sqrt(d)")
    for dim, sigma in points:
        ax.scatter([dim], [sigma], zorder=3, color="#d64545", s=45)
        ax.annotate(f"d={dim}: {sigma}", (dim, sigma), textcoords="offset points", xytext=(8, 6))
    for i, (name, value) in enumerate(sorted(signals.items(), key=lambda kv: -kv[1])):
        ax.axhline(value, ls="--", lw=1, color="#3b6fb5")
        dy = 5 if i == 0 else -14  # the two lines are 0.008 apart: label one up, one down
        ax.annotate(
            f"{name} = {value}",
            (600, value),
            textcoords="offset points",
            xytext=(0, dy),
            ha="right",
        )
    ax.set_xscale("log")
    ax.set_xlabel("embedding dimension d (log)")
    ax.set_ylabel("std of cosine between unrelated pairs")
    ax.set_title("Below d ~= 86 the instrument's noise exceeds the signal it ranks")
    ax.legend(frameon=False)
    fig.tight_layout()
    for ext in ("png", "svg"):
        fig.savefig(outdir / f"fig1-noise-floor.{ext}", dpi=200)
    plt.close(fig)


def main() -> int:
    """Regenerate every figure into ``output/figures/``.

    Returns
    -------
    int
        0 on success.
    """
    outdir = ROOT / "output" / "figures"
    outdir.mkdir(parents=True, exist_ok=True)
    fig1_noise_floor(outdir)
    print(f"figures written to {outdir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
