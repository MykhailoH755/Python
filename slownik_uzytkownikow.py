uzytkownicy = {
    "Adam": 25,
    "Ewa": 30,
    "Jan": 22,
    "Kasia": 27
}

def dodaj_uzytkownika(imie, wiek):
    if imie in uzytkownicy:
        print(f"Użytkownik {imie} już istnieje.")
    else:
        uzytkownicy[imie] = wiek
        print(f"Dodano użytkownika {imie} ({wiek} lat).")

def usun_uzytkownika(imie):
    if imie in uzytkownicy:
        del uzytkownicy[imie]
        print(f"Usunięto użytkownika {imie}.")
    else:
        print(f"Użytkownik {imie} nie istnieje.")

def wyswietl_uzytkownikow():
    print("\nLista użytkowników:")
    for imie, wiek in uzytkownicy.items():
        print(f"{imie}: {wiek} lat")

dodaj_uzytkownika("Marta", 24)
usun_uzytkownika("Jan")
wyswietl_uzytkownikow()
