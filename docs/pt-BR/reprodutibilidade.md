# Reprodutibilidade

## Contrato

- **Determinismo bit-a-bit:** toda medição usa `numpy.random.default_rng` com seed fixa
  (`SEED = 0`). `tests/test_determinism.py` trava o contrato.
- **Número publicado = asserção de teste:** cada valor citado pelo artigo existe como
  assert em `tests/` — se o código e `data/measurements.json` divergirem, o CI quebra.

## Passo a passo

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r code/requirements.txt
python code/noise_floor.py     # d= 32  sigma=0.177 / d=384  sigma=0.051
python code/gap_intensity.py   # ghost gap = 0.177 -> curiosity 0.58
pip install pytest && pytest   # 11 testes, todos verdes
```

Ambiente de referência: Python >= 3.11, numpy >= 1.24 (macOS e Linux; o CI roda em
ubuntu-latest com Python 3.12).

## O que NÃO é reproduzível daqui

As medições in-situ do daimon (embedder hash real, sinais de ranking, temperatura) exigem o
código privado. Elas entram como dados declarados em `data/measurements.json`, com data de
verificação — a demo numpy reproduz o mesmo piso teórico de forma independente.
