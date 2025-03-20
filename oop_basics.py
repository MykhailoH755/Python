class Samochod:
    def __init__(self, marka, kolor):
        self.marka = marka  
        self.kolor = kolor  

    def pokaz_informacje(self):
        print(f"Samochód: {self.marka}, Kolor: {self.kolor}")

auto1 = Samochod("Toyota", "Czerwony")  
auto2 = Samochod("BMW", "Czarny")  

auto1.pokaz_informacje()  
auto2.pokaz_informacje()  

print("Zmieniamy kolor samochodu...")
auto1.kolor = "Niebieski"  
auto1.pokaz_informacje()  
