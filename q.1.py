
num = int(input())
def even_or_odd(num):
    if num % 2 == 0:
        print(num, 'is even.')
    else:
        print(num, 'is odd.')
even_or_odd(num)


def shape_name(num):
    if num < 3 or num > 10:
        print("Your input should be between 3 and 10.")
    elif num == 3:
        print("The shape is a triangle.")
    elif num == 4:
        print("The shape is a quadrilateral.")
    elif num == 5:
        print("The shape is a pentagon.")
    elif num == 6:
        print("The shape is a hexagon.")
    elif num == 7:
        print("The shape is a heptagon.")
    elif num == 8:
        print("The shape is an octagon.")
    elif num == 9:
        print("The shape is a nonagon.")
    elif num == 10:
        print("The shape is a decagon.")

num = int(input())

shape_name(num)






def days_in_month(month):
    if month < 1 or month > 12:
        print("Your input should be between 1 and 12")
    elif month == 2:
        print("The month has 28 or 29 days in it.")
    elif month in {4, 6, 9, 11}:
        print("The month has 30 days in it.")
    else:
        print("The month has 31 days in it.")

month = int(input())

days_in_month(month)




def leap_year(year):
    if year % 400 == 0:
        print(f"{year} is leap.")
    elif year % 100 == 0:
        print(f"{year} is not leap.")
    elif year % 4 == 0:
        print(f"{year} is leap.")
    else:
        print(f"{year} is not leap.")

year = int(input())

leap_year(year)
