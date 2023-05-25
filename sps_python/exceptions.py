import json


class SPSExceptionNetwork(Exception):
    pass


class SPSExceptionJSON(Exception):
    pass


class SPSExceptionValue(Exception):
    pass


class SPSException:

    def __init__(self, velikost: int):
        self.velikost = velikost

    def obvod(self):
        try:
            self.kontrola_promenne()
        except SPSExceptionValue:
            pass
        return self.velikost * 4

    def obsah(self):
        try:
            self.kontrola_promenne()
            return self.velikost * self.velikost
        except SPSExceptionValue:
            pass
        return self.velikost * self.velikost

    def kontrola_promenne(self):
        try:
            je_cislo = int(self.velikost)
        except ValueError:
            print(f"Promenna {self.velikost} ma by cislo nikolv text")
            raise SPSExceptionValue
        return True

    def with_open_soubor(self, nazev: str):
        self.content = []
        with open(nazev, mode="rt") as fd:
            self.content = fd.read()
        print(self.content)

    def convert_to_json(self):
        try:
            json_data = json.loads(self.content)
        except json.decoder.JSONDecodeError as exc:
            raise SPSExceptionJSON(f"data jsou: {self.content} and {exc.msg}")
