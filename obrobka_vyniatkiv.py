try:
    num = int(input("Введіть число: "))  
    print(f"Ваше число: {num}")
except ValueError:
    print("Помилка! Це не число.")
else:
    print("Все добре! Ви ввели коректне число.")
finally:
    print("Ця частина коду виконається завжди.")
