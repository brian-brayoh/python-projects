# PA106/G/9556/20
# Mutwiri Brian Muthomi
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


operator = input("Enter an operator (+, -, *, /, or %): ")


if operator == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operator == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operator == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operator == '/':
    if num2 != 0:  
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
elif operator == '%':
    if num2 != 0:  
        result = num1 % num2
        print(f"{num1} % {num2} = {result}")
    else:
        print("Error: Modulus by zero is not allowed.")
else:
    print("Invalid operator. Please enter a valid operator (+, -, *, /, or %).")
