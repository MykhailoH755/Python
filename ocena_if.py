
ocena = input("Podaj swoją ocenę (0-100 lub 'brak' jeśli nie oceniono): ").strip()

if ocena.isdigit():
    ocena = float(ocena)

    if 90 <= ocena <= 100:
        print("Ocena: 5 ocena Bardzo dobra  ")
    elif 75 <= ocena < 90:
        print("Ocena:  4.5 Dobra  ")
    elif 50 <= ocena < 75:
        print("Ocena:  4 ocena Dostateczna  ")
    elif 30 <= ocena < 50:
        print("Ocena: 3 ocena Mierna  ")
    elif 0 <= ocena < 30:
        print("Ocena: 2 jcena Niedostateczna  ")
    else:
        print("Niepoprawna ocena! Podaj liczbę z zakresu 0-100.")
    
elif ocena.lower() == "brak":
    print("Brak oceny, spróbuj następnym razem!")
else:
    print("Niepoprawne dane! Podaj liczbę z zakresu 0-100 lub 'brak'.")
