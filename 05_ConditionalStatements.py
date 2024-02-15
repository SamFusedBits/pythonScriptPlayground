# 1. Write a python program to determine the grade based on a user's input score. 
# Give the grades starts from First class with Distinction to Fail as per the score percentage.

score = float(input("Enter your score percentage: "))
if score >= 90:
    grade = "First class with Distinction"
elif score >= 80:
    grade = "First class"
elif score >= 70:
    grade = "Second class"
elif score >= 60:
    grade = "Third class"
elif score >= 40:
    grade = "Pass"
else:
    grade = "Fail"
    print(f"Your grade is: {grade}")

# 2. Write a python program for number comparison. Get two numbers from the users and compare the numbers and display the result. 
# Result could be Like greater than, less than or equal numbers.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num1 > num2:
 result = "greater than"
elif num1 < num2:
 result = "less than"
else:
 result = "equal to"
 print(f"{num1} is {result} {num2}")

# 3. Write a python program to check for leap years. Take a year as an input from the user and depending on the input display appropriate messages.

year = int(input("Enter a year: "))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
 print(f"{year} is a leap year.")
else:
 print(f"{year} is not a leap year.")

# 4. Write a python program for age classifier.
# - If the age is less than zero, then display the message as Invalid age.
# - If the age in between zero to 18 then Minor.
# - If the age is in between 18 to 65 then Adult.
# - If the age is above 65 then Senior Citizen.

age = int(input("Enter your age: "))
if age < 0:
 print("Invalid age")
elif age <= 18:
 print("Minor")
elif age <= 65:
 print("Adult")
else:
 print("Senior Citizen")


#Assignment(Try this yourself)
# 5. WAPP to create a basic grading system for multiple subjects. 
# It calculates the average grade and provides a final grade based on the average score.
# If students got less the 35 marks in any of the subjects, then the overall result will be FAIL.

subject1 = float(input("Enter marks for Python: "))
subject2 = float(input("Enter marks for Web Technology 1: "))
subject3 = float(input("Enter marks for Database Applications: "))
subject4 = float(input("Enter marks for Business Statistics: "))
subject5 = float(input("Enter marks for Artificial Intelligence: "))
average_score = (subject1 + subject2 + subject3 + subject4 + subject5) / 5
if subject1 < 35 or subject2 < 35 or subject3 < 35 or subject4 < 35 or subject5 < 35:
 result = "FAIL"
else:
 if average_score >= 90:
    result = "A+"
 elif average_score >= 80:
    result = "A"
 elif average_score >= 70:
    result = "B"
 elif average_score >= 60:
    result = "C"
 else:
    result = "D"

print("\n***************************************************************************")
print("\t\t\t\tGrading Summary")
print("\n***************************************************************************")
print(f"\t\t\tSubject\t\t\tMarks")
print("\n---------------------------------------------------------------------------")
print(f"\t\t\tPython\t\t\t{subject1}")
print(f"\t\t\tWeb Technology 1c\t{subject2}")
print(f"\t\t\tDatabase Applications\t{subject3}")
print(f"\t\t\tBusiness Statistics\t{subject4}")
print(f"\t\t\tArtificial Intelligence\t{subject5}")
print("\n---------------------------------------------------------------------------")
print(f"\t\t\tFinal Grade:\t{average_score:.2f}")
print(f"\t\t\tResult:\t\t{result}")
print("\n---------------------------------------------------------------------------")
if result=="FAIL":
 print("You didn't meet the passing criteria in one or more subjects.")
else:
 print("You have successfully passed all subjects.")


