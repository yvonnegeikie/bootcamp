# What is a library or module?

# This module provides various functions to manipulate time values.
 #import (module) time
import time 



"Predict, then Run, and then Investigate"
name = "John"
print(name)

# invoke the sleep method from the time module
time.sleep(1)

"To Do: Can you explain what the 'time.sleep(3)' line of code does?"


print(f"Printed \n{name}")

# print(f"The directory\n{dir()}")


print(f"The directory with the time module\n{dir(time)}")



#  # import (module) random
import random

"syntax : variable = method(start and end values)"
# Return random integer in range [a, b], including both end points.
randomNumber = random.randint(1,10)

print(f"The random value is: {randomNumber}")


# "Modify "
# "To Do: Task 1: Use randint from random module to generate random numbers"
# # Modify the code above to generate ramdom numbers between 25 to 50


# import math # import (module) math
# This module provides access to the mathematical functions defined by the C standard
import math
radius = float(input("Enter the radius: "))
# rp = pow(radius,2)
# area = math.pi * rp
area = math.pi * pow(radius,2)

# "Predict, then Run, and then Investigate"

print(f"The area is {area}")

# Method 1
# Round (round) a number to a given precision in decimal digits.
print(f"The area displayed is rounded to 2 decimal places {round(area,2)}")

# Method 2
print(f"The area displayed is rounded to 3 decimal places {area:.3f}")

"Use the math module to round up or down"

roundDown = math.floor(area)
print(f"The area displayed is rounded down to the nearest whole number {roundDown}")

roundUp = math.ceil(area)
print(f"The area displayed is rounded up to the nearest whole number {roundUp}")

  


