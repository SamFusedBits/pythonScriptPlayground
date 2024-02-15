# - Resources to follow :
#   - [Real Python - Python Loops](https://realpython.com/python-for-loop/)

#1. Write a python program to Print the multiplication table for a given number.

 # Request user input for the number
number = int(input("Enter a number to display its multiplication table: "))
print(f"Multiplication Table for {number}:")
for i in range(1, 11):
 result = number * i
 print(f"{number} x {i} = {result}")

# 2. Write a python program to create a countdown timer using a while loop. You can use sleep method for delay in displaying numbers.

import time
countdown = int(input("Enter countdown time (in seconds): "))
while countdown > 0:
 print(countdown)
 time.sleep(1) # Sleep for 1 second
 countdown -= 1
 print("Time's up!")

# 3. Write a python program to print a simple pattern using nested loops.
# *
# **
# ***
# ****
# *****

rows = 5
 # Loop to print the pattern 37
for i in range(1, rows + 1):
 for z in range(1, i + 1):
    print("*", end="")
    print()

#Assignment(Try this yourself)
# 4. Write a python program to print a * pyramid
# pattern using nested loops.
#  *
#  **
#  ***
# ****
# *****

rows = 5
 # Loop to print the pyramid pattern
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * i)

#Assignment(Try this yourself)
# 5. Write a python program to calculate the sum of numbers from 1 to N (e.g., N = 5)

N = int(input("Enter a positive integer (N): "))
 # Initialize the sum
total = 0
for i in range(1, N + 1):
 total += i
 print(f"The sum of numbers from 1 to {N} is: {total}")
