# Bibliography — the two literatures that do not cite each other

Curated from a multilingual prior-art scan (EN/JA/FR/DE/PT, 2026-08-01, PRISMA-S spirit:
native-language probes per tradition, full snowball over the 778 works citing Burda et al.
and the 36 citing Mavor-Parker, integral reading of the three candidates that could have
killed the thesis). Result: **no work formalizes measurement-noise capture in the
intrinsic-motivation instrumentation of LLM agents** — zero-hit probes replicated in three
independent cells. This scan is honest, not a proof of non-existence.

## The classic noisy-TV line (RL)

- Oudeyer, P.-Y.; Kaplan, F. — *What is intrinsic motivation? A typology of computational
  approaches* (2007). doi:10.3389/neuro.12.006.2007
- Schmidhuber, J. — *Driven by Compression Progress* (2008). arXiv:0709.0674
- Burda, Y. et al. — *Large-Scale Study of Curiosity-Driven Learning* (2018).
  arXiv:1808.04355 — the noisy-TV experiment.
- Burda, Y. et al. — *Exploration by Random Network Distillation* (2018). arXiv:1810.12894
- Mavor-Parker, A. N. et al. — *How to Stay Curious while avoiding Noisy TVs* (ICML 2022).
  arXiv:2102.04399
- Salgado (DeepMind Paris) et al. — *Curiosity in Hindsight* (2023). hal-05413279 —
  formalizes noisy-TV, classic RL only.

## Recent formalizations — still 100% RL, no LLM

- *BAMDP Shaping* (2024). arXiv:2409.05358
- Hou; An; Du — *Beyond Noisy-TVs: Noise-Robust Exploration via Learning Progress
  Monitoring* (2025). arXiv:2509.25438 — **watch**: nearest neighbor to crossing into LLM.

## The LLM-agent instrumentation line (patches the pathology without naming it)

- *Curiosity-Driven Red-Teaming* (CRT, ICLR 2024). arXiv:2402.19464 — novelty by embedding
  cosine + temperature; patches noise capture with a gibberish detector, never names it.
- *DiveR-CT* (2024). arXiv:2405.19026 — documents "novelty stagnation" of the CRT metric.
- Colas, C. et al. — *LMA3* (2023). arXiv:2305.12487 — novelty = nearest-neighbor over
  SentenceBERT embeddings, zero occurrences of noise/distractor/aleatoric: affirmative
  evidence of the gap.
- *MAGELLAN* (Flowers, 2025). arXiv:2502.07709 — the learning-progress-to-LLM-embeddings
  bridge; zero treatment of noise in 114k chars of fulltext.
- *Measuring LLM Novelty* (2025). arXiv:2504.09389 — U-effect of temperature; "variation
  is not meaningful novelty". Closest neighboring insight, without the noisy-TV frame.

## The dual and the neighbors (2026 — the window is narrowing)

- *The Dark Room in the Reward Channel* (2026). arXiv:2607.21273 — formalizes the DUAL
  (dark-room collapse) for LLM agents under GRPO; frames noisy-TV only rhetorically
  ("two poles of one failure family"), no experiment or proposition on the noisy side.
  **Watch**: author has preregistered predictions pending.
- Elmoznino, E. et al. — *Can In-Context Learning Support Intrinsic Curiosity?* (2026).
  arXiv:2606.19476 — inevitable biases of learning progress via ICL; neighboring theory.
- Ban et al. — survey (2026). doi:10.2139/ssrn.6748619 — noisy-TV appears in RL/world-model
  contexts only; the LLM bridge is one qualitative sentence (§4.3.2), no formalization.

## Japanese tradition (context)

- JSAI 2026, "Noisy-TV 問題" in world-model RL. CiNii crid:1390871867482437248 — treats it
  as RL, not as LLM instrumentation.
