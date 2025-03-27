def pobierz_liczbe(prompt):
    while True:
        try:
            liczba = int(input(prompt))
            return liczba
        except ValueError:
            print("To nie jest poprawna liczba. Spróbuj ponownie.")

def oblicz_sume(liczba1, liczba2):
    return liczba1 + liczba2

def oblicz_roznice(liczba1, liczba2):
    return liczba1 - liczba2

def oblicz_dobutek(liczba1, liczba2):
    return liczba1 * liczba2

def oblicz_czesc(liczba1, liczba2):
    if liczba2 != 0:
        return liczba1 / liczba2
    else:
        return "Nie można dzielić przez zero!"

def oblicz_min(liczba1, liczba2):
    return min(liczba1, liczba2)

def oblicz_max(liczba1, liczba2):
    return max(liczba1, liczba2)

def oblicz_srednia(liczba1, liczba2):
    return (liczba1 + liczba2) / 2

imie = input("Jak masz na imię? ")
while True:
    try:
        wiek = int(input("Ile masz lat? "))
        if wiek <= 0:
            print("Wiek musi być liczbą dodatnią. Spróbuj ponownie.")
            continue
        break
    except ValueError:
        print("To nie jest poprawna liczba. Spróbuj ponownie.")

print(f"Cześć, {imie}!")
print(f"Za rok będziesz mieć {wiek + 1} lat.")

liczba1 = pobierz_liczbe("Podaj pierwszą liczbę: ")
liczba2 = pobierz_liczbe("Podaj drugą liczbę: ")

suma = oblicz_sume(liczba1, liczba2)
roznica = oblicz_roznice(liczba1, liczba2)
dobutek = oblicz_dobutek(liczba1, liczba2)
czesc = oblicz_czesc(liczba1, liczba2)
minimum = oblicz_min(liczba1, liczba2)
maksimum = oblicz_max(liczba1, liczba2)
srednia = oblicz_srednia(liczba1, liczba2)

print(f"Suma tych liczb to: {suma}")
print(f"Różnica tych liczb to: {roznica}")
print(f"Iloczyn tych liczb to: {dobutek}")
print(f"Iloraz tych liczb to: {czesc}")
print(f"Najmniejsza liczba to: {minimum}")
print(f"Największa liczba to: {maksimum}")
print(f"Średnia tych liczb to: {srednia}")

