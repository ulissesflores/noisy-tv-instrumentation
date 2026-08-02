# Pre-registration — DRAFT (pending operator approval)

> [!WARNING]
> Draft pre-registration for the paper in progress on measurement-noise capture in the
> intrinsic-motivation instrumentation of LLM agents. Predictions become binding when this
> file is sealed in the first tagged release. Amendments must be dated, never rewritten.

## Registered predictions (falsifiable)

- **P1 — noise floor propagates.** In any agent whose curiosity/novelty trigger reads
  gaps from embedding cosines at dimension `d`, a repetition control (N cycles under an
  *identical* stimulus) will measure a displacement floor compatible with `~1/sqrt(d)`.
  Readings below that floor are indistinguishable from instrument noise.
  *Falsified if:* the repetition control shows a floor well below `1/sqrt(d)` without any
  explicit noise treatment (normalization, aggregation, thresholding) explaining it.
- **P2 — ghost gap at saturation.** With coverage forced to saturation (nothing left to
  learn), a Goldilocks trigger (`4*g*(1-g)`) fed by a `d=32` embedder will read intensity
  `~0.58` (of 1.0 max); raising the embedder to `d=384` drops the ghost intensity below
  `0.20`. *Falsified if:* measured ghost intensity at `d=32` is far below `0.58`.

## Decision rule (the gate)

If a repetition control in **two or more independent agent frameworks** shows the noise
floor does *not* propagate into the deployed novelty metric (because a mitigation is
already standard practice), the core claim is limited to unmitigated instrumentations and
the paper is reframed — or amputated if the mitigated case is the norm.

## Amendments

- 2026-08-02 — initial draft (pre-release; not yet binding).
