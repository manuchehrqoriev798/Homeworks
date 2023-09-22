#   In a file named einstein.py, implement a program in Python that prompts the
#   user for mass as an integer (in kilograms) and then outputs the equivalent
#   number of Joules as an integer.
#   Example:
#       Input: 50
#       Output: "The equivalent number of Joules for 50 kilograms is:
#               4493775893684088200 Joules"
#   Hint: Even if you haven’t studied physics (recently or ever!), you might
#   have heard that E=m*c*c, wherein E represents energy (measured in Joules),
#   m represents mass (measured in kilograms), and c represents the speed of
#   light (measured approximately as 299792458 meters per second). Essentially,
#   the formula means that mass and energy are equivalent.

mass = int(input())
c = 299792458
result = mass * c * c
print(result)