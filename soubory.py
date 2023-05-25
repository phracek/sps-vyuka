#!/usr/bin/python

import os
import json
import yaml
from pathlib import Path

#1) Ukol pro otevreni souboru jako parameter
#2) vypis obsah soubory /etc/passwd a zobraz Uzivatelske jmeno a implicitni bash
#3) zapis do souboru budto jako text nebo jako pole.
#4) +++++ Pomoci pathlib zobrazit obsah adresaru a napsat co je soubor a co adresar


def otevri_soubor_open(nazev: str, mode: bool = False) -> str:
    if not os.path.exists(nazev):
        print(f"soubor {nazev} neexistuje.")
        return 1
    descriptor = open(nazev, mode="rt")
    if mode:
        lines = descriptor.read()
    else:
        lines = descriptor.readlines()
    descriptor.close()
    return lines


def write_soubor_open(nazev: str, text) -> str:
    descriptor = open(nazev, mode="wt")
    descriptor.write(text)
    descriptor.close()


def with_open_soubor(nazev: str):
    new_cnt = []
    with open(nazev, mode="rt") as fd:
        content = fd.read()
        new_cnt = content + "sesse"
    print(new_cnt)

# print(otevri_soubor_open("/tmp/sps.txt"))
# json_data = otevri_soubor_open("/tmp/sps.json", mode=True)
# print(json.loads(json_data))
# yaml_data = otevri_soubor_open("/tmp/sps.yaml", mode=True)
# print(yaml.safe_load(yaml_data))


cesta = Path("/tmp/sps.txt")
os.path.isdir()
print(cesta.is_dir())
if not cesta.exists():
    print("Neexistuje")
with_open_soubor("/tmp/sps.txt")