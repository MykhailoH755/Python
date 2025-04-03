user_input = input("Подай оцінки через пробіл: ")

numbers = [int(x) for x in user_input.split()]


def grade_converter(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


letter_grades = [grade_converter(score) for score in numbers]


max_num = max(numbers)
min_num = min(numbers)
average = sum(numbers) / len(numbers)

def find_top_students(students):
    max_grade = max(students.values())  
    top_students = [name for name, grade in students.items() if grade == max_grade]  
    return top_students, max_grade


students = {
    "Марія": 85,
    "Олександр": 92,
    "Ірина": 78,
    "Віктор": 95,
    "Андрій": 95
}


top_students, top_grade = find_top_students(students)


numbers.sort()
print("Відсортовані оцінки:", numbers)
print(f"Максимальне число: {max_num}")
print(f"Мінімальне число: {min_num}")
print(f"Студенти з максимальною оцінкою ({top_grade}): {', '.join(top_students)}")
print(f"Середнє значення оцінок: {average:.2f}")
print("Літерні оцінки: ", letter_grades)

