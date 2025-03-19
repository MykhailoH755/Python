def dzielenie(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Nie można dzielić przez zero!"
    except ValueError:
        return "Proszę wprowadzić liczby!"
    
liczba1 = input("Podaj pierwszą liczbę: ")
liczba2 = input("Podaj drugą liczbę: ")

try:
    liczba1 = int(liczba1)
    liczba2 = int(liczba2)
    wynik = dzielenie(liczba1, liczba2)
    print("Wynik dzielenia:", wynik)
except ValueError:
    print("Wprowadzono niepoprawne dane!")

print("Koniec programu.")
