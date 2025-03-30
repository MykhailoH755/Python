
przedmioty = ("Matematyka", "Historia", "Biologia", "Chemia", "Informatyka")


def wyswietl_przedmioty():
    print("\nLista przedmiotów:")
    for przedmiot in przedmioty:
        print(f"- {przedmiot}")

def sprawdz_przedmiot(nazwa):
    if nazwa in przedmioty:
        print(f"Przedmiot {nazwa} jest na liście.")
    else:
        print(f"Przedmiotu {nazwa} nie ma na liście.")


def przedmiot_na_pozycji(index):
    if 0 <= index < len(przedmioty):
        return przedmioty[index]
    else:
        return "Niepoprawny indeks"


wyswietl_przedmioty()
sprawdz_przedmiot("Historia")
print(f"Przedmiot na pozycji 2: {przedmiot_na_pozycji(2)}")
sprawdz_przedmiot("Fizyka")
