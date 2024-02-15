#I. Simple Commands:

#- 1. Write a program that prints your name.

name = "Sahil"
print("My name is:", name)

#- 2. Create a program that displays "Hello, World!" on the screen.

print("Hello, World!")

#- 3. Write a program that asks the user for their age and then prints it

age = input("Enter your age: ")
print("Your age is:", age)

#- 4. Write a Python program to add odd numbers from 1-10.

sum = 0
for number in range(1, 11):
    if number % 2 != 0:
        sum+=number
        print("The sum of odd numbers from 1 to 10 is:", sum)

#- 5. Write a Python program to get the Fibonacci series between 0 to 50. 

x,y=0,1
while x<=50:
    print(x, end="")
    x,y = y,x+y

#II. Mathematical Operators:

#- 1. Create a program to calculate the area of a rectangle given its length and width.

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
print("The area of the rectangle is:", area)

#- 2. Write a program that calculates the volume of a cube using its side length.

side_length = float(input("Enter the side length of the cube: "))
volume = side_length ** 3
print("The volume of the cube is:", volume)

#- 3. Create a simple calculator program that can perform addition, subtraction, multiplication, and division.

print("Enter Option")
print("Enter 'add' for addition")
print("Enter 'sub' for subtraction")
print("Enter 'mul' for multiplication")
print("Enter 'div' for division")
 # User enter the input
choice = input("Enter operation: ")
if choice in ('add', 'sub', 'mul', 'div'):
 num1 = float(input("Enter first number: "))
 num2 = float(input("Enter second number: "))
if choice == 'add':
 result = num1 + num2
 print("Result:", result)
elif choice == 'sub':
 result = num1 - num2
 print("Result:", result)
elif choice == 'mul':
 result = num1 * num2
 print("Result:", result)
elif choice == 'div':
 result = num1 / num2
 print("Result:", result)
else:
 print("Invalid input")

#III. Range:

#- 1. Write a program that prints all even numbers between 1 and 50.

for number in range(2, 51, 2):
 print(number)

#- 2. Create a program that generates a list of squares of numbers from 1 to 10 using a loop.

squares = [number ** 2 for number in range(1, 11)]
print("Squares of numbers from 1 to 10:", squares)

#- 3. Write a program to calculate the sum of all numbers between 1 and 100.

sum_of_numbers=0
for number in range(1, 101):
    sum_of_numbers+=number
    print("Sum of numbers between 1 and 100:", sum_of_numbers)
