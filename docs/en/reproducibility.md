# Reproducibility

## Contract

- **Bit-for-bit determinism:** every measurement uses `numpy.random.default_rng` with a
  fixed seed (`SEED = 0`). `tests/test_determinism.py` enforces the contract.
- **Published number = test assertion:** every value the article cites exists as an assert
  in `tests/` — if the code and `data/measurements.json` ever drift apart, CI breaks.

## Step by step

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r code/requirements.txt
python code/noise_floor.py     # d= 32  sigma=0.177 / d=384  sigma=0.051
python code/gap_intensity.py   # ghost gap = 0.177 -> curiosity 0.58
pip install pytest && pytest   # 11 tests, all green
```

Reference environment: Python >= 3.11, numpy >= 1.24 (macOS and Linux; CI runs on
ubuntu-latest with Python 3.12).

## What is NOT reproducible from here

The daimon in-situ measurements (real hash embedder, ranking signals, temperature) require
the private codebase. They enter as declared data in `data/measurements.json`, with
verification dates — the numpy demo reproduces the same theoretical floor independently.
