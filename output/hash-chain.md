# Provenance hash chain

**chain_hash:** `2dfab1c6a4345fb082249eac90b6cde6a9e882c4deadbda895181e76d929ecb5`

Recompute and compare with: `python make_provenance.py --verify`

## Hashed (the claim depends on these bytes)

| File | SHA-256 |
|---|---|
| `code/gap_intensity.py` | `1af637d0338ada048f781e98973bfbdfded095fdc7a3b17896dd23e4ec7546b1` |
| `code/noise_floor.py` | `324a53b5d8c8fa5dc6309f48e5cba03f5e201cff57b50741de5da4de5e77e727` |
| `code/requirements.txt` | `a83a2a4ed7ab2e022b9b8a83cfa2b8cf52cc243006c597e8b96f90a8365590ac` |
| `data/PREREGISTRATION.md` | `07770c261e455afecd3e5d7cfece574032c24db3c19df77430d2af05a9a941ce` |
| `data/measurements.json` | `ffb9d97abafa8743df8e598057742b80889ef4b5623aff44ce211b06d51840d7` |
| `output/results.json` | `06ed40ab9734adf0f9cd5abe1e7c2e5e132f2f6fd1472c0542e9edcc77fc1bdd` |
| `tests/test_determinism.py` | `e80fed45a51237fbef6c469975e000bd1c05d95b53fb657c67a3dbcd63271b12` |
| `tests/test_gap_intensity.py` | `52de7edeaf497d2a8df9b65d5df367d7cb32bd0c54c63d9105d0be92dc811386` |
| `tests/test_measurements.py` | `57d22c87c7a1d5240fec2acf778da3728f9b99c33426ca630a6e699df932f3ce` |
| `tests/test_noise_floor.py` | `6e148760c119c4b6445a8979c096f9245972d8432d06a62384a636c953d6c3c6` |

## Informational (NOT hashed)

- Generated: 2026-08-02
- Python: 3.14.6 on Darwin arm64
- Figures (`output/figures/`) and `requirements.lock` are excluded so the
  chain survives machine and renderer changes; results are what is sealed.
