tekst = input("Wprowadź tekst: ")

slowa = tekst.split()

unikalne_slowa = set(slowa)

posortowane_slowa = sorted(unikalne_slowa)

print("\nUnikalne słowa w tekście:")
for slowo in posortowane_slowa:
    print(slowo)

print(f"\nLiczba unikalnych słów: {len(unikalne_slowa)}")
