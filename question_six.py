# PA106/G/9556/20
# MUtwiri Brian Muthomi
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


if num2 == 0:
    print("Error: Division by zero is not allowed.")
else:
    
    if num1 > num2:
        larger_number = num1
        smaller_number = num2
    else:
        larger_number = num2
        smaller_number = num1

    
    result = larger_number / smaller_number

    
    print(f"{larger_number} / {smaller_number} = {result}")
