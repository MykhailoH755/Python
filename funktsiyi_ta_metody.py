def print_list(lst):
    print("Список:")
    for item in lst:
        print(item)


def get_average(lst):
    return sum(lst) / len(lst)


def get_positive_numbers(lst):
    positives = []
    for num in lst:
        if num > 0:
            positives.append(num)
    return positives


numbers = []


for i in range(5):
    n = int(input(f"Введи число №{i+1}: "))
    numbers.append(n)


print_list(numbers)

avg = get_average(numbers)
print("Середнє значення:", avg)

positives = get_positive_numbers(numbers)
print("Додатні числа:", positives)


