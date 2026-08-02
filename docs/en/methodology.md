# Methodology

## What is measured

Two quantities, both dimensionless:

1. **Cosine noise floor** — standard deviation of the cosine similarity between pairs of
   random unit vectors in dimension `d`. Theory: ~`1/sqrt(d)`. Measured by
   `code/noise_floor.py` over 20,000 pairs with a fixed seed: `0.177` at `d=32` and
   `0.051` at `d=384`.
2. **Ghost gap** — the most benign possible scenario for a Goldilocks curiosity trigger
   (`4*g*(1-g)`): true coverage of 1.0 (nothing left to learn) read with 1 sigma of
   `d=32` embedder static. Result: `g = 0.177` -> intensity `0.58` of a 1.0 maximum
   (`code/gap_intensity.py`).

## Provenance of the real-system numbers

The values `0.177`/`0.050` (hash embedder at `d=32`, ONNX model at `d=384`), the ranking
signals `0.108` (one full day of memory decay) and `0.100` (one point of importance), and
the sampling temperature `0.8` come from the calibration of **daimon**, a private project
by the author. The original code is not published; this repository contains only minimal
rewrites that preserve the logic and reproduce the numbers, plus the measured data with
verification dates (`data/measurements.json`).

## Declared limits

- The numpy demo uses random Gaussian vectors — the ideal case of the theory. Real text
  embeddings are anisotropic; the daimon floor (0.177 at d=32) matches the theory by
  construction of its hash embedder, not by universal accident.
- The ghost-gap scenario is the *most benign* one (1 sigma). Larger tails occur with the
  expected Gaussian frequency.
