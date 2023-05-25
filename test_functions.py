#!/bin/python
import pytest

import functions


@pytest.mark.parametrize(
    "strana,hodnota",
    [
        (4, 16),
        (5, 20),
        (6, 24)
    ]
)
def test_obvod_obdelniku_spravny(strana, hodnota):
    assert functions.obvod_ctverce(strana) == hodnota


def test_obvod_obdelniku_spatny():
    assert functions.obvod_ctverce(4) != 15


def test_obvod_obdelniku_spatny_velke_cislo():
    with pytest.raises(Exception):
        functions.obvod_ctverce(26) == 121
