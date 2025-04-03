user_input = input("Введи числа через пробіл")


numbers = [int(x) for x in user_input.split() ]


max_num = max(numbers)
min_num = min(numbers)

average = sum(numbers) / len(numbers)

numbers.sort()  


print("Відсортовані числа:", numbers)
print(f"Максимальне число: {max_num}")
print(f"Мінімальне число: {min_num}")
print(f"Середнє значення: {average:.2f}")

