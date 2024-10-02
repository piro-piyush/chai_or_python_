# Problem: Keep asking the user for input until they enter a number between 1 and 10.

while True:
    number = int(input("Enter a number : "))
    if number > 0 or number < 10:
        break
    else:
        print("Invalid number, try again")
