"""The noise floor reproduces the published sigmas and the 1/sqrt(d) law."""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "code"))

from noise_floor import noise_floor  # noqa: E402


def test_sigma_d32_matches_published_value():
    """d=32 reproduces the article's 0.177 to three decimals."""
    assert round(noise_floor(32), 3) == 0.177


def test_sigma_d384_matches_published_value():
    """d=384 reproduces the article's 0.051 to three decimals."""
    assert round(noise_floor(384), 3) == 0.051


def test_inverse_sqrt_scaling():
    """The floor tracks the 1/sqrt(d) theory within 5% for several dims."""
    for dim in (32, 64, 128, 384):
        assert abs(noise_floor(dim) - 1.0 / math.sqrt(dim)) / (1.0 / math.sqrt(dim)) < 0.05
