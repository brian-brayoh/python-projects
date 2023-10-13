# PA106/G/9556/20
# Mutwiri Brian Muthomi
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


if num1 > num2:
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif num2 > num1:
    if num2 != 0: 
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
