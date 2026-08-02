# Metodologia

## O que é medido

Duas grandezas, ambas adimensionais:

1. **Piso de ruído do cosseno** — desvio-padrão da similaridade de cosseno entre pares de
   vetores aleatórios unitários em dimensão `d`. Teoria: ~`1/sqrt(d)`. Medido por
   `code/noise_floor.py` com 20.000 pares e seed fixa: `0,177` em `d=32` e `0,051` em
   `d=384`.
2. **Lacuna-fantasma** — o cenário mais benigno possível para um gatilho de curiosidade
   Goldilocks (`4·g·(1-g)`): cobertura real igual a 1,0 (nada a aprender) lida com 1 sigma
   de chuvisco do embedder de `d=32`. Resultado: `g = 0,177` -> intensidade `0,58` de um
   máximo de 1,0 (`code/gap_intensity.py`).

## Proveniência dos números do sistema real

Os valores `0,177`/`0,050` (embedder hash em `d=32` e modelo ONNX em `d=384`), os sinais de
ranking `0,108` (um dia de decaimento) e `0,100` (um ponto de importância) e a temperatura
de amostragem `0,8` vêm da calibração do **daimon**, projeto privado do autor. O código
original não é publicado; este repositório contém apenas reescritas mínimas que preservam a
lógica e reproduzem os números, mais os dados medidos com data de verificação
(`data/measurements.json`).

## Limites declarados

- A demo numpy usa vetores gaussianos aleatórios — o caso ideal da teoria. Embeddings de
  texto reais têm anisotropia; o piso medido no daimon (0,177 em d=32) coincide com a
  teoria por construção do embedder hash, não por acaso universal.
- O cenário da lacuna-fantasma é o *mais benigno* (1 sigma). Caudas maiores ocorrem com a
  frequência gaussiana esperada.
