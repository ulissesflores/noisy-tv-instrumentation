# Reproducibility — step by step

The contract itself — determinism, "published number = test assertion", the two seals, and what
is frozen and cannot be re-run — lives in [`../../REPRODUCIBILITY.md`](../../REPRODUCIBILITY.md),
the single source. This page is the walkthrough only.

## Step by step

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r code/requirements.txt
python code/noise_floor.py     # d= 32  sigma=0.177 / d=384  sigma=0.051
python code/gap_intensity.py   # ghost gap = 0.177 -> curiosity 0.58
pip install pytest && pytest   # all green
```

Reference environment, CI matrix, and the limits of what is reproducible from here:
[`../../REPRODUCIBILITY.md`](../../REPRODUCIBILITY.md).
