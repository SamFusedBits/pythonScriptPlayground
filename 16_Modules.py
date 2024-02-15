# - Resources to follow :
#   - [Python Documentation - Modules](https://docs.python.org/3/tutorial/modules.html)

# 1. Choose two different modules from the Python standard library. 
# Write a Python script that integrates both modules to perform a specific task or solve a problem.

import datetime
import os
current_datetime = datetime.datetime.now()
print(f"Current date and time: {current_datetime}")
current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")

#Assignment(Try this yourself)
# 2. Create a Python module that acts as a simple calculator. 
# Include functions for addition, subtraction, multiplication, and division.
# Write a script to import and use this module to perform arithmetic operations.

# mycalculator.py
def add(x, y):
 return x + y
def subtract(x, y):
 return x - y
def multiply(x, y):
 return x * y
def divide(x, y):
 if y != 0:
    return x / y
 else:
    return "Error: Division by zero"
# script.py
import sys
sys.path.append(r'\mycalculator.py') # Replace with the actual path of the file in your system
import mycalculator
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))
result_add = mycalculator.add(x, y)
result_subtract = mycalculator.subtract(x, y)
result_multiply = mycalculator.multiply(x, y)
result_divide = mycalculator.divide(x, y)
print(f"Addition: {result_add}")
print(f"Subtraction: {result_subtract}")
print(f"Multiplication: {result_multiply}")
print(f"Division: {result_divide}")

# 3. Create a Python script that uses the math module to calculate the area and circumference of a circle, 
# the volume of a sphere, and the hypotenuse of a right-angled triangle. Allow the user to input relevant parameters.

import math
radius = float(input("Enter the radius of the circle: "))
triangle_side1 = float(input("Enter the first side of the triangle: "))
triangle_side2 = float(input("Enter the second side of the triangle: "))
sphere_radius = float(input("Enter the radius of the sphere: "))
area_circle = math.pi * radius**2
circumference_circle = 2 * math.pi * radius
hypotenuse_triangle = math.sqrt(triangle_side1**2 + triangle_side2**2)
volume_sphere = (4/3) * math.pi * sphere_radius**3
print(f"Area of the circle: {area_circle}")
print(f"Circumference of the circle: {circumference_circle}")
print(f"Hypotenuse of the triangle: {hypotenuse_triangle}")
print(f"Volume of the sphere: {volume_sphere}")

#Assignment(Try this yourself)
# 4. Write a Python script that generates a random password of a specified length. Utilize the random module to include a mix of uppercase
# letters, lowercase letters, numbers, and special characters.

import random
import string
def generate_password(length):
 characters = string.ascii_letters + string.digits + string.punctuation
 password = ''.join(random.choice(characters) for _ in range(length))
 return password
password_length = int(input("Enter the length of the password: "))
random_password = generate_password(password_length)
print(f"Random Password: {random_password}")

# 5. Develop a simple task scheduler using the time module. Allow the user to input tasks along with their scheduled execution times. 
# The program should execute the tasks at the specified times.

import time
def schedule_task(task, scheduled_time):
 while True:
    current_time = time.strftime("%H:%M:%S")
    print(f"Current time: {current_time}")
 if current_time == scheduled_time:
    print(f"Executing task: {task}")
    break
 time.sleep(1)
task1 = input("Enter Task 1: ")
time1 = input("Enter Task 1 scheduled time (Hrs:Min:Sec): ")
task2 = input("Enter Task 2: ")
time2 = input("Enter Task 2 scheduled time (Hrs:Min:Sec): ")
print("Waiting for tasks to execute...")
schedule_task(task1, time1)
schedule_task(task2, time2)
