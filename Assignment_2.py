# Module 3: Control Structures in Python
 
# Task 1: Check if a Number is Even or Odd
# Problem Statement:  Write a Python program that:
# 1. 	Takes an integer input from the user.
a = int(input("Enter the number: "))
# 2. 	Checks whether the number is even or odd using an if-else statement.
# 3. 	Displays the result accordingly.
if(a % 2)==0:
     print("Even number",a)
else:
    print("odd number",a)

# Task 2: Sum of Integers from 1 to 50 Using a Loop
 
# Problem Statement: Write a Python program that:
# 1.   Uses a for loop to iterate over numbers from 1 to 50.
for i in range(1,50):
     print('Apple')
# 2.   Calculates the sum of all integers in this range.
# 3.   Displays the final sum.
i=list(range(1,50))
print("The sum of numbers from 1 to 50 is:",sum(i))
