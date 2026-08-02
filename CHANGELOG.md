# Changelog

All notable changes to this repository are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versions follow
[Semantic Versioning](https://semver.org/).

## [Unreleased]

## [1.0.0] — 2026-08-02

First public release (nothing was published before this tag; the internal
staging iterations are folded in here).

### Added

- `code/noise_floor.py` — deterministic demo of the cosine noise floor
  (`sigma = 0.177` at d=32, `0.051` at d=384, ~`1/sqrt(d)`).
- `code/gap_intensity.py` — the Goldilocks trigger and the ghost-gap scenario
  (gap `0.177` fabricated by noise -> curiosity `0.58/1.0`).
- `data/measurements.json` — every number cited by the article, with method,
  source and verification dates.
- `tests/` — pytest suite pinning the published numbers, the scaling law,
  determinism, and code/data consistency.
- `BIBLIOGRAPHY.md` — the two disconnected literatures + prior-art scan summary.
- Scientific metadata: `CITATION.cff`, `codemeta.json`, `.zenodo.json`.
- Provenance layer: `make_provenance.py` (single `chain_hash` over code + data +
  results; `output/hash-chain.md` + `provenance.json`) and `run_all.py` as the
  single replication entry point.
- `REPRODUCIBILITY.md` (two-seals contract), `requirements.lock` (verbatim
  freeze), `data/PREREGISTRATION.md` (draft falsifiable predictions + gate),
  `ROADMAP.md`.
- Figures as code: `scripts/make_figures.py` (claim-mapped) ->
  `output/figures/fig1-noise-floor.{png,svg}`.
- CI (`.github/workflows/ci.yml`): verification-first (committed chain verify +
  full replication on Python 3.11/3.12) with lint as a separate job.

### Changed

- License: MIT -> dual **Apache-2.0** (code) + **CC BY 4.0** (content), matching
  the lab's published standard; added `NOTICE` and `LICENSES/`.
- `CLAUDE.md` (local agent instructions) moved out of the public tree via
  `.gitignore`; `Makefile` removed in favor of `run_all.py`.
