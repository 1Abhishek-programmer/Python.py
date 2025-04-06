# Module 4: Functions & Modules in Python 
# Task 1: Calculate Factorial Using a Function 
# Problem Statement: Write a Python program that:
# 1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
def factorial(n):
    if n<2:
        return 1
    else:
        return (n * factorial(n-1))
result = factorial(5)
print('Factorial of 5 is:',result)
  

# Task 2: Using the Math Module for Calculations
 
# Problem Statement: Write a Python program that:
# 1.   Asks the user for a number as input.
# 2.   Uses the math module to calculate the:
# o   Square root of the number
# o   Natural logarithm (log base e) of the number
# o   Sine of the number (in radians)
# 3.   Displays the calculated results.
import math
a =int(input("Enter a number:"))
sqrt_a = math.sqrt(a)
print("Square root:",sqrt_a)
log_a =math.log(a)
print("Logarithm:",log_a)
sin_a =math.sin(a)
print("Sin:",sin_a)