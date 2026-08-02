"""Determinism is a contract: same seed, same bits, every run."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "code"))

from noise_floor import noise_floor  # noqa: E402


def test_noise_floor_is_deterministic():
    """Two calls with the default seed return the identical float."""
    assert noise_floor(32) == noise_floor(32)
    assert noise_floor(384) == noise_floor(384)


def test_seed_changes_the_sample_not_the_law():
    """A different seed moves the estimate only within the published tolerance."""
    assert abs(noise_floor(32, seed=1) - noise_floor(32, seed=0)) < 0.005
