kilometers = float(input())
km_to_cm = 100000
km_to_mile = 0.621371
cm_to_yard = 0.010936
inch_to_cm = 2.54
foot_to_cm = 30.48

# Convert the distance to other units
centimeters = kilometers * km_to_cm
feet = centimeters / foot_to_cm
inches = centimeters / inch_to_cm
yards = centimeters * cm_to_yard
miles = kilometers * km_to_mile


print(centimeters, feet, inches, yards, miles)
