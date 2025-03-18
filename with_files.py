hobby = input("Podaj swoje hobby: ")

with open("hobby.txt", "a") as file:
    file.write(hobby + "\n")

print("Hobby zapisane!")

with open("hobby.txt", "r") as file:
    print("Twoje hobby:")
    print(file.read())
