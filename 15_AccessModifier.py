# - Resources to follow :
#  - [Python OOP - Access Modifiers](https://www.pythonoop.com/python-oop-concepts/access-modifiers/)

# Write a python program to demonstrate access
# modifiers in:
# (a) Private
# (b) Public
# (c) Protected   
# #Explore on the internet

#(a) Private
class myClass:
 def __init__(self):
    self.__private_var = 42 #Private variable

 def get_private_var(self):
    return (str(self.__private_var) + ("This is a private method"))
obj = myClass()
#Accessing the private variable using name mangling
print(obj._myClass__private_var)
#Accessing the private method
print(obj.get_private_var())

#(b) Public
class myclass:
 def print(self):
    print("This is a public method")
obj=myclass()
obj.print()

#(c) Protected
class baseclass:
 def __init__(self):
    self._protectedVar = 40
 def _protected_method(self):
    print("This is a Protected Method")
class derivedclass(baseclass):
 def access_protected(self):
    print(self._protectedVar)
    self._protected_method()

derived_object = derivedclass()
derived_object.access_protected()
print(derived_object._protectedVar)
derived_object._protected_method()