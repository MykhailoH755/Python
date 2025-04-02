user_input = input("Введіть кілька чисел через пробіл: ")

numbers = [int(x) for x in user_input.split()]

for number in numbers:
    if number % 2 == 0:
        print(f"{number} є парним числом.")
    else:
        print(f"{number} є непарним числом.")


