# Reprodutibilidade — passo a passo

O contrato em si — determinismo, "número publicado = asserção de teste", os dois selos, e o que
está congelado e não pode ser re-rodado — vive em
[`../../REPRODUCIBILITY.md`](../../REPRODUCIBILITY.md), a fonte única. Esta página é só o
passo a passo.

## Passo a passo

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r code/requirements.txt
python code/noise_floor.py     # d= 32  sigma=0.177 / d=384  sigma=0.051
python code/gap_intensity.py   # ghost gap = 0.177 -> curiosity 0.58
pip install pytest && pytest   # todos verdes
```

Ambiente de referência, matrix do CI e os limites do que é reproduzível daqui:
[`../../REPRODUCIBILITY.md`](../../REPRODUCIBILITY.md).
