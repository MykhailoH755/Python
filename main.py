numbers = [float(input("Enter the first number: ")), float(input("Enter the second number: "))]
operator = input("Enter an operation (+, -, *, /): ")


if operator == "+":
    result = numbers[0] + numbers[1]

elif operator == "-":
    result = numbers[0] - numbers[1]

elif operator == "*":
    result = numbers[0] * numbers[1]

elif operator == "/":
    if numbers[1] != 0:
        result = numbers[0] / numbers[1]

    else:
        result = "Error! Division by zero."
else:
    result = "Unknown operation."
    

print("Result:", result)

