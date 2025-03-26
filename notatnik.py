notes = {}

while True:
    cmd = input("(1) Додати (2) Переглянути (3) Вийти: ")

    if cmd == "1":
        notes[input("Назва: ")] = input("Текст: ")

    elif cmd == "2":
        print("\nНотатки:")
        for t, c in notes.items():
            print(f"{t}: {c}")

    elif cmd == "3":
        break

