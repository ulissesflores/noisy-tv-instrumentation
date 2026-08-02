"""Ghost-gap demo: a curiosity trigger firing on pure measurement noise.

``gap_intensity`` is a minimal rewrite of the daimon's knowledge-gap trigger —
the classic Goldilocks form ``4*g*(1-g)``, maximal at intermediate gaps, zero
at both extremes. Feed it a gap fabricated entirely by the ``d=32`` embedding
noise floor (``sigma = 0.177``, see ``noise_floor.py``) and an agent with
literally nothing left to learn reads 0.58 out of a 1.0 maximum: the noisy TV,
reborn inside the ruler.
"""

SIGMA_D32 = 0.177
"""Measured cosine noise floor at d=32 (see data/measurements.json)."""


def gap_intensity(gap: float) -> float:
    """Map a knowledge gap to a curiosity intensity (Goldilocks curve).

    Parameters
    ----------
    gap : float
        Knowledge gap ``g`` as read by the instrument, expected in ``[0, 1]``.

    Returns
    -------
    float
        ``4*g*(1-g)`` — peaks at 1.0 for ``g = 0.5``; 0.0 at both extremes
        and for any ``g`` outside ``[0, 1]``.
    """
    return 4.0 * gap * (1.0 - gap) if 0.0 <= gap <= 1.0 else 0.0


def ghost_gap_scenario(sigma: float = SIGMA_D32) -> tuple[float, float]:
    """Compute the most benign scenario: full coverage minus one sigma of noise.

    Parameters
    ----------
    sigma : float, optional
        Cosine noise floor of the embedder feeding the coverage estimate.

    Returns
    -------
    tuple of float
        ``(gap, intensity)`` — the ghost gap fabricated by noise alone and
        the curiosity intensity the trigger pays for it.
    """
    true_coverage = 1.0
    read_coverage = true_coverage - sigma
    gap = 1.0 - read_coverage
    return gap, gap_intensity(gap)


def main() -> None:
    """Print the ghost-gap scenario at the measured d=32 noise floor."""
    gap, intensity = ghost_gap_scenario()
    print(f"ghost gap        = {gap:.3f}")
    print(f"curiosity signal = {intensity:.2f}  (max = 1.0)")


if __name__ == "__main__":
    main()
