# Problem 1: Timing Function Execution
# Problem: Write a decorator that measures the time a function takes to execute.
# Problem 2: Debugging Function Calls
# Problem: Create a decorator to print the function name and the values of its arguments every time the function is called.
# Problem 3: Cache Return Values
# Problem: Implement a decorator that caches the return values of a function, so that when it's called with the same arguments, the cached value is returned instead of re-executing the function.


import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result


@timer
def example_function(n):
    time.sleep(n)


example_function(2)
