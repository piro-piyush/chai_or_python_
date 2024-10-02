# Problem: Compute the factorial of a number using a while loop.

# number = int(input("Enter number : "))
# factorial = 1

# for i in range(1, number + 1):
#     factorial *= i

# print(factorial)

number = int(input("Enter number : "))
factorial = 1

while number > 0:
    factorial *= number
    number -= 1

print(factorial)
