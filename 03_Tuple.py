# - Resources to follow :
#  - [Real Python - Python Lists](https://realpython.com/python-lists-tuples/)
#      - [GeeksforGeeks - Python List Operations](https://www.geeksforgeeks.org/python-list/)


# 1. Write a python program to create a tuple of your favourite fruits.
# - Print the tuple.
# - Access and print individual elements of the tuple.
# - Attempt to modify an element in the tuple and observe the error.
# - Calculate and print the length of the tuple

# Create a tuple of favorite fruits
favorite_fruits = ("Apple", "Guava", "Strawberry", "Pineapple", "Mango")
 # Print the tuple
print("Favorite Fruits Tuple:", favorite_fruits)
 # Access and print individual elements
print("First Fruit:", favorite_fruits[0])
print("Second Fruit:", favorite_fruits[1])
print("Third Fruit:", favorite_fruits[2])
print("Fourth Fruit:", favorite_fruits[3])
print("Fifth Fruit:", favorite_fruits[4])
 # Attempt to modify an element (will raise an error)
favorite_fruits[0] = "cherry"
 # Calculate and print the length of the tuple
print("Length of Tuple:", len(favorite_fruits))

# 2. Write a python program to create a tuple containing a student's name and them scores in:
# - Use tuple unpacking to extract and print the student's name and each subject score separately.
# - Calculate and print the average score for the student.

 # Create a tuple containing a student's name and scores in three subjects
student_info = ("Alice", 90, 85, 92)
 # Tuple unpacking to extract and print individual elements
name, score1, score2, score3 = student_info
print("Student Name:", name)
print("Subject 1 Score:", score1)
print("Subject 2 Score:", score2)
print("Subject 3 Score:", score3)
 # Calculate and print the average score
average_score = (score1 + score2 + score3) / 3
print("Average Score:", average_score)

# 3. Write a python program to create a list of tuples, each containing a student's name and their exam scores.
# - Sort the list of tuples in ascending order based on the average score (consider using a custom sorting key).
# - Print the sorted list of tuples.

 # Function to calculate the average score from a list of scores
def calculate_average(scores):
    return sum(scores) / len(scores)
 # Create a list of tuples containing student names and exam scores
student_scores = [
 ("Sahil", [90, 85, 88]),
 ("David", [78, 92, 86]),
 ("Bob", [85, 79, 91]),
 ("Ayushman", [92, 88, 84]),
 ]
 # Define a custom sorting function based on average score
def custom_sorting_key(student):
    name, scores = student
    return calculate_average(scores)
 # Sort the list of tuples based on the average score in ascending order
    sorted_student_scores = sorted(student_scores, key=custom_sorting_key)
 # Print the sorted list of tuples
    for student in sorted_student_scores:
        name, scores = student
        average_score = calculate_average(scores)
        print("Name=", name, "and average score=", average_score)

# 4. Write a python program to create two tuples containing days of the week (e.g., weekdays and weekends).
# - Concatenate the two tuples to create a single tuple representing all days of the week.
# - Create a new tuple by repeating one of the original tuples multiple times.

# Create two tuples containing days of the week
weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
weekends = ("Saturday", "Sunday")
 # Concatenate the two tuples to create a single tuple representing all days of the week
all_days = weekdays + weekends
 # Create a new tuple by repeating one of the original tuples multiple times
repeated_weekdays = weekdays * 2
 # Print the concatenated and repeated tuples
print("All Days of the Week:", all_days)
print("Repeated Weekdays:", repeated_weekdays)

# 5. Create Python functions that demonstrate tuple packing and unpacking.
# - Implement a function that takes multiple arguments and returns them as a tuple (packing).
# - Implement a function that receives a tuple as an argument and unpacks it, printing the elements.

# Function for tuple packing (packing multiple arguments into a tuple)
def pack_arguments(arg1, arg2, arg3, arg4):
    return (arg1, arg2, arg3, arg4) # Return the arguments as a tuple
 # Function for tuple unpacking (printing elements of a tuple)
def unpack_and_print(a_tuple):
  for item in a_tuple:
    print(item)
 # Example usage:
 # Packing multiple arguments into a tuple
my_tuple = pack_arguments('Apple', 10, 'Pi value', 3.14)
 # Unpacking the tuple and printing its elements
unpack_and_print(my_tuple)
