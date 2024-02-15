# 1. Write a python program to demonstrate Inheritance in animals, Call subclasses with parent class member function.

class Animal:
 def __init__(self, name):
    self.name = name
 def speak(self):
    print(f"{self.name} makes a sound")
class Dog(Animal):
 def speak(self):
    print(f"{self.name} barks")
class Cat(Animal):
 def speak(self):
    print(f"{self.name} meows")
dog = Dog("Buddy")
cat = Cat("Whiskers")
dog.speak()
cat.speak() 

#Assignment(Try this yourself)
# 2. Write a python program to demonstrate inheritance in employee. Call subclass with parent class member function

class Employee:
 def __init__(self, name, emp_id):
    self.name = name
    self.emp_id = emp_id
 def display_info(self):
    print(f"Employee ID: {self.emp_id}\nName: {self.name}")
 class Manager(Employee):
  def display_info(self):
    super().display_info()
    print("Position: Manager")
 # Creating an instance and calling member functions
 employee = Employee("Mack", 1001)
 manager = Manager("Sahil", 2001)
 employee.display_info()
 print("\n")
 manager.display_info()
