# PA106/G/9556/20
# Mutwiri Brian Muthomi
import math


def calculate_rectangle():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    perimeter = 2 * (length + width)
    return "Rectangle", f"Length: {length}, Width: {width}", f"Area: {area}", f"Perimeter: {perimeter}"


def calculate_circle():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * (radius ** 2)
    perimeter = 2 * math.pi * radius
    return "Circle", f"Radius: {radius}", f"Area: {area}", f"Perimeter: {perimeter}"


def calculate_triangle():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    hypotenuse = math.sqrt(base**2 + height**2)
    area = 0.5 * base * height
    perimeter = base + height + hypotenuse
    return "Right-Angled Triangle", f"Base: {base}, Height: {height}", f"Area: {area}", f"Perimeter: {perimeter}"


print("Select a figure to compute area and perimeter:")
print("1. Rectangle")
print("2. Circle")
print("3. Right-Angled Triangle")


choice = int(input("Enter your choice (1/2/3): "))


if choice == 1:
    figure, dimensions, area, perimeter = calculate_rectangle()
elif choice == 2:
    figure, dimensions, area, perimeter = calculate_circle()
elif choice == 3:
    figure, dimensions, area, perimeter = calculate_triangle()
else:
    print("Invalid choice. Please select 1, 2, or 3.")
    exit()


print(f"Figure: {figure}")
print(f"Dimensions: {dimensions}")
print(f"{area}")
print(f"{perimeter}")
