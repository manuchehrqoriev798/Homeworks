"""
This module contains functions from the previous lab session (Lab 2). There is
no guarantee that these functions work correctly. You need to test the
functions and make sure that they do not have bugs.

Requested tasks:
    - Specifications:
        - Write a full specification inside each function listed below.
        - The specification should contain a short description, parameter
          information, and a precondition.

    - Testing:
        - Write a unit test "functions_test.py" that tests all the functions
          listed below.
        - For each function, at least 10 different representative test cases
          should be included in the unit test.
        - The functions contain bugs. You need to identify and fix the bugs.
"""

"""
The function acres receives as float numbers the width and length in feet of a
farmer’s field, and then returns as a float number the area of the field in
acres. Example: Input: 60.5, 20.7. Output: 0.028749999999999998.
"""
def acres(a,b):
    c = a*(b/43560)
    return c

"""
The function circle_area receives as float number the radius of a circle,
and then returns as float number the area of the circle.
Example: Input: 6.7. Output: 141.0260942196458.
"""
def circle_area(a):
    from math import pi
    area = pi*a**2
    return area

"""
The function sphere_volume receives as float number the radius of a sphere,
and then returns as float number the volume of the sphere.
Example: Input: 6.7. Output: 1259.8331083621692.
"""
def sphere_volume(a):
    from math import pi
    volume = (4/3) * pi * (a**3)
    return volume


"""
The function convert receives as float number the temperature in centigrade,
and then returns as float number the temperature in fahrenheit.
Example: Input: 14.0. Output: 57.2.
"""
def to_fahrenheit(temperature_in_celsius: float) -> float:
    return (9 * temperature_in_celsius / 5.0) + 32


"""
The function greet receives a name as string, and then prints a greeting to the
name. Example: Input: "Jane". Output: "Hello Jane!".
"""
def greet(name):
    text = "Hello " + name + "!"
    print(text)


"""
The function sm receives a positive integer, n, and then
returns as the sum of all of the integers from 1 to n.
name_campus_test.py
"""
def sm(n: int) -> int:
    return n * (n + 1) // 2


"""
The function sort_integers receives three integer numbers,
and then sorts them from smallest to largest.
Example: Input: 10, 7, 19. Output: 7, 10, 19.
"""
def sort_integers(a, b, c):
    smallest = min(a, b, c)
    largest = max(a, b, c)
    middle = a + b + c - smallest - largest
    return smallest, middle, largest


"""
The function swap receives two integer numbers,
and then swaps the two numbers.
Example: Input: 3, 4. Output: 4, 3.
"""
def swap(a, b):
    a, b = b, a
    return a, b
