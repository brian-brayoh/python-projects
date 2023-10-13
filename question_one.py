# PA106/G/9556/20
# Mutwiri Brian Muthomi
beer_prices = {
    1: 200,
    2: 280,
    3: 320,
    4: 180
}


print("* * * * Jamal and Daughters Pub * * * *")
print("Beer Brand Price")
print("1) Tusker 200/=")
print("2) Pilsner 280/=")
print("3) Smirnoff Ice 320/=")
print("4) White Cap 180/=")


choice = int(input("Enter your choice: "))


if choice not in beer_prices:
    print("Invalid choice. Please select a valid option (1, 2, 3, or 4).")
else:
    
    quantity = int(input(f"How many bottles of {'Tusker' if choice == 1 else 'Pilsner' if choice == 2 else 'Smirnoff Ice' if choice == 3 else 'White Cap'} do you want? "))

    
    total_cost = beer_prices[choice] * quantity

    
    print(f"{quantity} bottles of {'Tusker' if choice == 1 else 'Pilsner' if choice == 2 else 'Smirnoff Ice' if choice == 3 else 'White Cap'} will cost you Kshs. {total_cost}")
