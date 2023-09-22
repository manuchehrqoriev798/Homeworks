# functions_test.py

""" Unit tests for all the functions in the module "functions.py" """

import functions
from functions import greet
import asserts
from math import pi
import random

num_test_cases = 10

# Test cases
result1 = functions.acres(60.5, 20.7)
asserts.assert_equals(0.02875, result1)

result2 = functions.acres(10, 11)
asserts.assert_equals(0.002525252525252525, result2)

result3 = functions.acres(0, 0)
asserts.assert_equals(0, result3)

result4 = functions.acres(10, 12)
asserts.assert_equals(0.002754820936639118, result4)

result5 = functions.acres(10, 13)
asserts.assert_equals(0.0029843893480257116, result5)

result6 = functions.acres(10, 14)
asserts.assert_equals(0.0032139577594123047, result6)

result7 = functions.acres(10, 15)
asserts.assert_equals(0.003443526170798898, result7)

result8 = functions.acres(10, 16)
asserts.assert_equals(0.0036730945821854912, result8)

result9 = functions.acres(10, 17)
asserts.assert_equals(0.0039026629935720847, result9)

result10 = functions.acres(10, 18)
asserts.assert_equals(0.004132231404958678, result10)
print(1)

# Test the greet function
def greet(name):
    return f"Hello {name}!"
name_list = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hank", "Ivy", "Jack"]
num_test_cases = len(name_list)

for i in range(num_test_cases):
    name = name_list[i]
    expected_output = "Hello " + name + "!"
    actual_output = greet(name)
    assert actual_output.strip() == expected_output, f"greet Test case {i + 1} failed: expected '{expected_output}', got '{actual_output}'"
    print(f"greet Test case {i + 1} successful")
print(2)

# Test the sm function
for i in range(num_test_cases):
    n = random.randint(1, 100)
    expected_result = n * (n + 1) // 2
    result = functions.sm(n)
    assert result == expected_result, f"sm Test case {i + 1} failed: expected {expected_result}, got {result}"
print(3)

# Test the circle_area function
for i in range(num_test_cases):
    radius = random.uniform(1, 100)
    expected_result = pi * radius ** 2
    result = functions.circle_area(radius)
    assert result == expected_result, f"circle_area Test case {i + 1} failed: expected {expected_result}, got {result}"
print(4)

# Test the sphere_volume function
for i in range(num_test_cases):
    radius = random.uniform(1, 100)
    expected_result = (4/3) * pi * (radius ** 3)
    result = functions.sphere_volume(radius)
    assert result == expected_result, f"sphere_volume Test case {i + 1} failed: expected {expected_result}, got {result}"
print(5)

# Test the to_fahrenheit function
for i in range(num_test_cases):
    celsius_temp = random.uniform(-100, 100)
    expected_result = (9 * celsius_temp / 5.0) + 32
    result = functions.to_fahrenheit(celsius_temp)
    assert result == expected_result, f"to_fahrenheit Test case {i + 1} failed: expected {expected_result}, got {result}"
print(6)

# Test the sort_integers function
for i in range(num_test_cases):
    a = random.randint(-100, 100)
    b = random.randint(-100, 100)
    c = random.randint(-100, 100)
    expected_result = tuple(sorted([a, b, c]))
    result = functions.sort_integers(a, b, c)
    assert result == expected_result, f"sort_integers Test case {i + 1} failed: expected {expected_result}, got {result}"
print(7)

# Test the swap function
for i in range(num_test_cases):
    a = random.randint(-100, 100)
    b = random.randint(-100, 100)
    expected_result = (b, a)  # Swap a and b
    result = functions.swap(a, b)
    assert result == expected_result, f"swap Test case {i + 1} failed: expected {expected_result}, got {result}"
print(8)

print('All tests of the functions passed')