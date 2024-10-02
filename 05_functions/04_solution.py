# Problem: Create a function that returns both the area and circumference of a circle given its radius.
import math


def circle(r):
    return 2 * math.pi * r, math.pi * r**2


print(circle(4))
