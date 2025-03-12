data = (1, 2, 3, "cześć", 5.5)


print("Pierwszy element:", data[0])
print("Ostatni element:", data[-1])


a, b, c, d, e = data
print("Rozpakowane wartości:", a, b, c, d, e)


if "cześć" in data:
    print("Słowo 'cześć' jest w krotce")


inna_krotka = (10, 20, 30)
polaczona_krotka = data + inna_krotka
print("Połączona krotka:", polaczona_krotka)


print("Liczba wystąpień 2 w krotce:", data.count(2))


print("Długość krotki:", len(data))
