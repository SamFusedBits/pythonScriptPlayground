# 1. Write a program to design a class to represent a car with attributes like make model year and speed each car object should contain 3
# methods which can start the engine accelerate and slow down the speed.

class Car:
 def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year
    self.speed = 0
 def start_engine(self):
    print(f"The {self.year} {self.make} {self.model}'s engine is started.")
 def accelerate(self):
    self.speed += 50
    print(f"The car is accelerating. Current speed: {self.speed} mph")
 def slow_down(self):
    self.speed -= 20
    print(f"The car is slowing down. Current speed: {self.speed} mph")
# Example use case:
my_car = Car("BMW", "Series 7", 2023)
my_car.start_engine()
my_car.accelerate()
my_car.slow_down()

#Assignment(Try this yourself)
# 2. Write a program to design a class to represent a rectangle with attributes like length and
# width each rectangle object should contain methods which can compare the rectangle and compute the area.

class Rectangle:
 def __init__(self, length, width):
     self.length = length
     self.width = width
 def compare(self, rect):
    if self.length == rect.length and self.width == rect.width:
        return "The rectangles are identical."
    else:
        return "The rectangles are not identical."
 def area(self):
    return self.length * self.width
 # Example use case:
rect1 = Rectangle(4, 5)
rect2 = Rectangle(5, 4)
print(rect1.compare(rect2))
print(f"Area of rect1: {rect1.area()}")

# 3. Design a class to represent a student with attributes like name, roll number, and marks.
# Create methods to calculate the grade and display student information.

class Student:
 def __init__(self, name, roll_number, marks):
    self.name = name
    self.roll_number = roll_number
    self.marks = marks
 def calculate_grade(self):
    if self.marks >= 90:
        return "A+"
    elif self.marks >= 80:
        return "A"
    elif self.marks >= 70:
        return "B"
    elif self.marks >= 60:
        return "C"
    else:
        return "F"
 def display_info(self):
    print(f"Name: {self.name}")
    print(f"Roll Number: {self.roll_number}")
    print(f"Marks: {self.marks}")
    print(f"Grade: {self.calculate_grade()}")
 # Example use case:
student = Student("Sahil", "28", 94)
student.display_info()

# 4. Implement a class for a library system with functions to add, delete, and search for books.

class Library:
 def __init__(self):
    self.books = []
 def add_book(self, book):
    self.books.append(book)
    print(f"{book} added to the library.")
 def delete_book(self, book):
    if book in self.books:
        self.books.remove(book)
        print(f"{book} deleted from the library.")
    else:
        print(f"{book} not found in the library.")
 def search_book(self, book):
    if book in self.books:
        print(f"{book} found in the library.")
    else:
        print(f"{book} not found in the library.")
 # Example use case:
library = Library()
library.add_book("Book 1")
library.add_book("Book 2")
library.search_book("Book 2")
library.delete_book("Book 1")

#Assignment(Try this yourself)
# 5. Develop a Python class for a simple bank account. Create a constructor that initializes the account holder's name and balance.
# Include methods for depositing and withdrawing money, and ensure that the balance cannot go negative. 
# Test the class by creating accounts and performing transactions.

class BankAccount:
 def __init__(self, account_holder, balance):
    self.account_holder = account_holder
    self.balance = balance
 def deposit(self, amount):
    if amount > 0:
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")
    else:
        print("Invalid deposit amount.")
 def withdraw(self, amount):
    if amount > 0:
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance:${self.balance}")
        else:
            print("Insufficient funds.")
    else:
        print("Invalid withdrawal amount.")
 # Example use case:
account = BankAccount("Sahil", 10000)
account.deposit(9000)
account.withdraw(3000)

#Assignment(Try this yourself)
# 6. Create a class for representing employees in an organization. The constructor should take parameters for employee name, employee ID,
# and salary. Implement a method that calculates an annual bonus based on the salary and a given bonus percentage. 
# Use this class to calculate the annual bonus for a set of employees.

class Employee:
 def __init__(self, name, employee_id, salary):
    self.name = name
    self.employee_id = employee_id
    self.salary = salary
 def calculate_annual_bonus(self, bonus_percentage):
  if bonus_percentage >= 0:
    annual_bonus = (bonus_percentage / 100) * self.salary
    return annual_bonus
  else:
    return 0
 # Example use case:
employee1 = Employee("Sahil", 101, 100000)
employee2 = Employee("John", 102, 75000)
bonus_percentage = 40
annual_bonus1 = employee1.calculate_annual_bonus(bonus_percentage)
annual_bonus2 = employee2.calculate_annual_bonus(bonus_percentage)
print(f"{employee1.name}'s annual bonus: ${annual_bonus1}")
print(f"{employee2.name}'s annual bonus: ${annual_bonus2}")
