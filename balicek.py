#/usr/bin/python

from sps_python.ctverec import Ctverec as Ct
from sps_python import ctverec

c1 = ctverec.Ctverec(4)
c2 = Ct(5)
print(c1)
print(c2)
print(c1 == c2)
print(c1 != c2)
