#!/bin/python
import pytest

vek = 47.0001
prvocisla = [1, 2, 3, 5, 7]
slovnik = {"a": 1, "b": 2}

print("Toto je promenna:")
print(f"Toto je promenna: {vek}")
print(prvocisla)
print(f"Prvocisla: {prvocisla}")
print("Prvocisla {} {}".format(prvocisla, vek))
print("Prvocisla {v} {s}".format(s=prvocisla, v=vek))
print(f"Prvocisla {prvocisla},{vek}")


def obvod_ctverce(strana: int, text: str = "Obvod") -> int:
    """
    Funkce na obvod_ctvrece
    :param strana: delka strany
    :param text: Hlavicka
    :return: Int -> Obvod ctvrece
    """
    print("neco")
    print(f"{text}: {4 * strana}")
    obvod = 4 * strana
    if obvod > 100:
        raise Exception
    return obvod


def test_obvod_obdelniku_spravny():
    assert obvod_ctverce(4) == 16


def test_obvod_obdelniku_spatny():
    assert obvod_ctverce(4) != 15


def test_obvod_obdelniku_spatny_velke_cislo():
    with pytest.raises(Exception):
        obvod_ctverce(26) == 121


def obvod_obdelniku(*args, **kwargs):
    print(args)
    print(kwargs)
    print(args[0])


obvod_ctverce(strana=5)

obvod_obdelniku(2,3,4,5,6,7, {"stav": "blbec"})


def obecna_funkce():
    for l in prvocisla:
        print(f"List: {l}")

    for key, value in slovnik.items():
        print(f"Key: {key} and value: {value}")

    for key in slovnik.keys():
        print(f"{key}: {slovnik[key]}")

    for count, key in enumerate(slovnik):
        print(f"Enu: {count}:{key}={slovnik[key]}")

print(f"Instance: {isinstance(prvocisla[0], int)}")

if __name__ == "__main__":
    obecna_funkce()
    obvod_obdelniku(1, 2, 3)
