# Module 4: Functions & Modules in Python 
# Task 1: Calculate Factorial Using a Function 
# Problem Statement: Write a Python program that:
# 1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
def facatorial(x):
    num = 1;
    for i in range(x):
        num*=i
    print(num)

facatorial(5)

    