# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

fruit = "Banana"
color = input("Enter the color of Banana : ")

color = color.capitalize()

# print(color)

if fruit == "Banana":
    if color == "Green":
        print("Banana is Unripe")
    elif color == "Yellow":
        print("Banana is Ripe")
    elif color == "Brown":
        print("Banana is Overripe")
    else:
        print("Wrong color of banana")
