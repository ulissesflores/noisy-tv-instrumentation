"""Noise floor of the cosine similarity between unrelated texts.

For random unit vectors in dimension ``d``, the cosine of an unrelated pair
does not sit at zero — it fluctuates around zero with standard deviation
approximately ``1/sqrt(d)``. This module reproduces the two floors discussed
in the article and measured in the daimon calibration: ``sigma ~= 0.177`` at
``d=32`` and ``sigma ~= 0.051`` at ``d=384``.

Deterministic: a fixed seed produces identical output on every run.
"""

import numpy as np

SEED = 0
"""Fixed RNG seed — determinism is a test-enforced property of this repo."""


def noise_floor(dim: int, n: int = 20_000, seed: int = SEED) -> float:
    """Measure the cosine noise floor between unrelated random vectors.

    Parameters
    ----------
    dim : int
        Dimension of the embedding space.
    n : int, optional
        Number of vector pairs to sample.
    seed : int, optional
        RNG seed; the default makes the measurement reproducible bit-for-bit.

    Returns
    -------
    float
        Standard deviation of the cosine similarity across the ``n`` pairs —
        the "static" an instrument reads when there is nothing to measure.
    """
    rng = np.random.default_rng(seed)
    a = rng.normal(size=(n, dim))
    b = rng.normal(size=(n, dim))
    a /= np.linalg.norm(a, axis=1, keepdims=True)
    b /= np.linalg.norm(b, axis=1, keepdims=True)
    return float((a * b).sum(axis=1).std())


def main() -> None:
    """Print the noise floor at d=32 and d=384 next to the expected values."""
    for dim, expected in [(32, 0.177), (384, 0.051)]:
        print(f"d={dim:>3}  sigma={noise_floor(dim):.3f}  (expected ~{expected})")


if __name__ == "__main__":
    main()
