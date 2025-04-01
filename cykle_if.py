print("Liczby od 1 do 10:")
for i in range(1, 11):
    print(i, end=" ")

print("\n\nPętla while – odliczanie:")
x = 5
while x > 0:
    print(f"Pozostało {x} sekund...")
    x -= 1

print("\nPętla for – iteracja po liście:")
owoce = ["jabłko", "banan", "pomarańcza", "winogrona"]
for owoc in owoce:
    print(f"Lubię {owoc}!")

print("\nPętla for z break:")
for liczba in range(1, 20):
    if liczba == 7:
        print("Zatrzymuję pętlę na 7!")
        break
    print(liczba, end=" ")

print("\n\nPętla while z continue:")
y = 0
while y < 10:
    y += 1
    if y % 2 == 0:
        continue  
    print(f"Nieparzysta liczba: {y}")
