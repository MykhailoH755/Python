class Pies:
    def __init__(self, imie, wiek, szczesliwy):
        self.imie = imie
        self.wiek = wiek
        self.szczesliwy = szczesliwy

    def pokaz_info(self):
        print(f"Pies: {self.imie}, Wiek: {self.wiek}, Szczęśliwy: {self.szczesliwy}")

pies1 = Pies("Reksio", 3, True)
pies1.pokaz_info()
