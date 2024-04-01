# This program calculates the perimeter and area of a triangle.
# The program uses Heron’s formula for finding the area of a triangle.

import math

a = float(input("Size of a side? "))
b = float(input("Size of b side? "))
c = float(input("Size of c side? "))


def heron_formula():
    perimeter = a + b + c
    # s is half the perimeter.
    s = perimeter / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return perimeter, area


if a + b > c and a + c > b and b + c > a:
    perimeter, area = heron_formula()
    print("Perimeter of the triangle is", perimeter)
    print("Area of the triangle is", area)
else:
    print("There exists no triangle with the given measurements.")
