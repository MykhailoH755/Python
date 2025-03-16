sciezka = "data/oxfile.txt"

def zapisz_hobby(hobby):
    with open(sciezka, 'a') as file:
        file.write(hobby + '\n')

def czytaj_hobby():
    with open(sciezka, 'r') as file:
        return file.readlines()

data = input("Hobby: ")

try:
    zapisane_hobby = czytaj_hobby()
except FileNotFoundError:
    zapisane_hobby = []

if data + '\n' not in zapisane_hobby:
    zapisz_hobby(data)
    print("Hobby zapisane!")
else:
    print("To hobby już istnieje w pliku!")
