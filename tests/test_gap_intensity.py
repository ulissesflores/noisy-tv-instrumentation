"""The Goldilocks trigger behaves as documented — including the ghost gap."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "code"))

from gap_intensity import gap_intensity, ghost_gap_scenario  # noqa: E402


def test_peak_at_intermediate_gap():
    """Curiosity is maximal (exactly 1.0) at g = 0.5."""
    assert gap_intensity(0.5) == 1.0


def test_zero_at_both_extremes():
    """Nothing-to-learn (g=0) and incomprehensible (g=1) both yield zero."""
    assert gap_intensity(0.0) == 0.0
    assert gap_intensity(1.0) == 0.0


def test_zero_outside_domain():
    """Values outside [0, 1] are clamped to zero, not extrapolated."""
    assert gap_intensity(-0.2) == 0.0
    assert gap_intensity(1.3) == 0.0


def test_ghost_gap_pays_more_than_half_maximum():
    """The d=32 noise floor alone buys 0.58 of a 1.0 maximum."""
    gap, intensity = ghost_gap_scenario()
    assert round(gap, 3) == 0.177
    assert round(intensity, 2) == 0.58
