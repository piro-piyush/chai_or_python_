# Problem: Create a recursive function to calculate the factorial of a number.


def factorial(n):
    if n > 0:
        return n * factorial(n - 1)
    else:
        return 1


print(factorial(5))
