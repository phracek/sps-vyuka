class Ctverec:
    def __init__(self, velikost_strany):
        self.velikost = velikost_strany

    def obvod(self):
        return self.velikost * 4

    def obsah(self):
        return self.velikost * self.velikost

    def __repr__(self):
        return f"<Ctverec>:velikost={self.velikost}"

    def __eq__(self, other):
        if not isinstance(other, Ctverec):
            raise Exception
        if self.velikost == other.velikost:
            return True
        return False
