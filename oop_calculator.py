class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Ділення на нуль неможливе"

num1 = int(input("Введіть перше число: "))
num2 = int(input("Введіть друге число: "))

calc = Calculator(num1, num2)

print(f"Сума: {calc.add()}")
print(f"Різниця: {calc.subtract()}")
print(f"Добуток: {calc.multiply()}")
print(f"Частка: {calc.divide()}")
