"""data/measurements.json stays consistent with the code and the article."""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "code"))

from gap_intensity import ghost_gap_scenario  # noqa: E402
from noise_floor import noise_floor  # noqa: E402

DATA = json.loads((Path(__file__).resolve().parents[1] / "data" / "measurements.json").read_text())


def test_noise_floor_entries_reproduce():
    """Every sigma_demo in the JSON is reproduced by code/noise_floor.py."""
    for entry in DATA["cosine_noise_floor"]["values"]:
        assert round(noise_floor(entry["dim"]), 3) == entry["sigma_demo"]


def test_ghost_gap_entry_reproduces():
    """The ghost-gap block matches code/gap_intensity.py exactly."""
    gap, intensity = ghost_gap_scenario()
    assert round(gap, 3) == DATA["ghost_gap"]["gap_from_noise"]
    assert round(intensity, 2) == DATA["ghost_gap"]["intensity"]


def test_signal_ordering_reading():
    """The d=32 floor really does exceed both ranking signals in the data."""
    values = {v["name"]: v["value"] for v in DATA["signals_vs_noise"]["values"]}
    floor = values["cosine noise floor, d=32"]
    assert floor > values["one full day of memory decay"]
    assert floor > values["one point of importance"]
