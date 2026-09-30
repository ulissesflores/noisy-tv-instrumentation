# Reproducibility

This file is the single source of the reproducibility contract.
[`docs/en/reproducibility.md`](docs/en/reproducibility.md) and
[`docs/pt-BR/reprodutibilidade.md`](docs/pt-BR/reprodutibilidade.md) carry the step-by-step
walkthrough only and point back here.

## Contract

- **Bit-for-bit determinism:** every measurement uses `numpy.random.default_rng` with a
  fixed seed (`SEED = 0`). `tests/test_determinism.py` enforces it.
- **Published number = test assertion:** every value the article cites exists as an assert
  in `tests/` — if the code and `data/measurements.json` ever drift apart, CI breaks.

Two seals, deliberately distinct (the "two seals" pattern):

1. **Reproducible derivation** — everything numpy: the noise floors, the scaling law, the
   ghost-gap scenario. Deterministic (seed 0); re-derived from scratch by `run_all.py` and
   asserted by the test suite on every CI run.
2. **Frozen evidence** — the daimon in-situ measurements (hash-embedder floor 0.177,
   ranking signals 0.108/0.100, sampling temperature 0.8). The daimon codebase is private:
   these values cannot be re-run here. They enter as *declared data* in
   `data/measurements.json` with verification dates, and the provenance chain proves they
   have not been altered since sealing — not that they can be regenerated.

## Track 1 — light (seconds)

```bash
pip install -r code/requirements.txt
python run_all.py
# [1/3] results.json written ... [2/3] test suite green ... [3/3] provenance verified
```

`run_all.py` rewrites the informational header of `output/hash-chain.md` (`Generated:`,
`Python:`), so `git status` reporting that file as modified after a run is **expected**: those
lines sit under `## Informational (NOT hashed)` and the `chain_hash` does not change. That the
seal survives a different machine and a different date is what the block is for.

## Track 2 — full

```bash
python make_provenance.py --verify   # integrity: chain_hash must match
pip install matplotlib && python scripts/make_figures.py   # regenerate figures
pip install ruff interrogate                               # style + docstring coverage
ruff format --check code tests scripts run_all.py make_provenance.py
ruff check code tests scripts run_all.py make_provenance.py
interrogate -f 100 code scripts run_all.py make_provenance.py
```

## Environment

Python >= 3.11, numpy >= 1.24 (CI: ubuntu-latest, Python 3.11 + 3.12). The environment
used for the sealed verification is frozen verbatim in `requirements.lock`
(informational, not hashed).

## What is frozen and cannot be re-run here

The daimon measurements (seal 2 above) and the prior-art scan behind
`BIBLIOGRAPHY.md` (executed 2026-08-01; searches are not reproducible bit-for-bit).
Everything else is seal 1: delete `output/`, run `python run_all.py`, get the same
numbers and the same `chain_hash` for the code+data set.
