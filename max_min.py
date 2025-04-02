user_input = input("Напиши цифри через пробіл: ")  

numbers = list(map(int, user_input.split()))

max_num = max(numbers)
min_num = min(numbers)

print(f"Максимальне число: {max_num}")
print(f"Мінімальне число: {min_num}")




