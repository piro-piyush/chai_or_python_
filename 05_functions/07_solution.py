# Problem: Write a function that takes variable number of arguments and returns their sum.
def my_sum(*args):
    return sum(args)


print(my_sum(1, 2, 3, 5))
