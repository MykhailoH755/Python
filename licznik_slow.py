tekst = "jabłko banan jabłko gruszka banan jabłko"
slowa = tekst.split()

licznik_slow = {} 
for slowo in slowa:
    licznik_slow[slowo] = licznik_slow.get(slowo, 0) + 1

print(licznik_slow)
