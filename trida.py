import os


test: int = 1


class SPSVyuka:

    def __init__(self, nazev: str, mode: bool = True):
        self.nazev = nazev
        self.mode = mode
        self._neni_trida = None

    def __str__(self):
        return f"SPSVyuka ma parametery: nazev={self.nazev} a mode je {self.mode} a property je {self._neni_trida}"

    def __repr__(self):
        return f"SPSVyuka:nazev={self.nazev};mode={self.mode}"

    def __eq__(self, other):
        pass

    def otevri_soubor_open(self) -> str:
        if not os.path.exists(self.nazev):
            print(f"soubor {self.nazev} neexistuje.")
            return 1
        descriptor = open(self.nazev, mode="rt")
        if self.mode:
            lines = descriptor.read()
        else:
            lines = descriptor.readlines()
        descriptor.close()
        print(lines)
        return lines

    @property
    def vrat_cely_popis(self):
        if not self._neni_trida:
            self._neni_trida = f"{self.nazev}-{self.mode}"
        return self._neni_trida

    @staticmethod
    def vypocti_obvod(mode = False):
        pass

    @staticmethod
    def vypocti_obsah(a, b=0, mode = True ):
        if mode == True:
            S = a*4
        else:
            S = (a+b)*2
        print(S)
        return S

    def vypocti_obvod_ctverec(self):
        SPSVyuka.vypocti_obsah(4, True)

    def vypocti_obvod_obdelnik(self):
        SPSVyuka.vypocti_obsah(4,5, False)

    def vypocti_obdelnik(self):
        pass


sps = SPSVyuka("/tmp/sps.txt")
sps.vrat_cely_popis
print(sps)
print(repr(sps))
sps.otevri_soubor_open()
sps.vypocti_obdelnik()
sps.vypocti_obvod_ctverec()
print(sps.mode)
print(sps.nazev)

