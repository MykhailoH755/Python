def powitanie():
    print("Cześć!")

powitanie()

def dodaj(a, b):
    return a + b

print(dodaj(3, 5))

def mnoz(a, b):
    return a * b

print(mnoz(4, 7))

maksimum = lambda a, b: a if a > b else b
print(maksimum(10, 20))

kwadrat = lambda x: x ** 2
print(kwadrat(6))

liczby = [1, 2, 3, 4, 5]
potegi = list(map(lambda x: x ** 2, liczby))
print(potegi)

parzyste = list(filter(lambda x: x % 2 == 0, liczby))
print(parzyste)

tekst = ["pies", "kot", "lew"]
tekst.sort(key=lambda x: len(x))
print(tekst)
