#/usr/bin/python

import sys

from sps_python.exceptions import SPSException

spse = SPSException(5)
print(spse.obsah())
print(spse.obvod())

spse = SPSException(10000)
if not spse.obsah():
    pass
print(spse.obvod())

spse = SPSException("2.2")
print(spse.obvod())


data = spse.with_open_soubor("/tmp/sps.json")
spse.convert_to_json()

sys.exit(0)
