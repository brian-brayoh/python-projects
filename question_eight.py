# PA106/G/9556/20
# Mutwiri Brian Muthomi
vehicle_speed = float(input("Enter the vehicle's speed (in kph): "))
speed_limit = float(input("Enter the speed limit (in kph): "))


excess_speed = vehicle_speed - speed_limit


if excess_speed < 30:
    fine = 2500
else:
    fine = 4000


print(f"Vehicle Speed: {vehicle_speed} kph")
print(f"Speed Limit: {speed_limit} kph")
print(f"Excess Speed: {excess_speed} kph")
print(f"Fine Levied: Kshs. {fine}")
