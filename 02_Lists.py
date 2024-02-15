# - Resources to follow :
# - [Real Python - Python Lists](https://realpython.com/python-lists-tuples/)
#      - [GeeksforGeeks - Python List](https://www.geeksforgeeks.org/python-list/)

#1. Create a Python program that performs basic list operations.
# - Create an empty list.
# - Add three different types of elements to the list (e.g., integers, strings, and floats).
# - Print the list.
# - Remove one element from the list.
# - Print the modified list.

# Create an empty list
my_list = []
 # Add elements to the list
my_list.append(45)
my_list.append("Hello")
my_list.append(3.14)

 # Print the list
print("Original List:", my_list)
 # Remove one element from the list
my_list.remove("Hello")
 # Print the modified list
print("Modified List:", my_list)

# 2. Write a python program for list indexing and slicing in Python.
# - Create a list of numbers from 1 to 10.
# - Print the first and last elements of the list.
# - Print a slice of the list containing elements from index 3 to 7.
# - Modify the list to replace the elements from index 5 to 9 with even numbers (e.g., 10, 12, 14, ...).
# - Print the modified list.

 # Create a list of numbers from 1 to 10
numbers = list(range(1, 11))
 # Print the first and last elements
print("First Element:", numbers[0])
print("Last Element:", numbers[-1])
 # Print a slice from index 3 to 7 (inclusive)
print("Slice from 3 to 7:", numbers[3:8])
 # Modify the list to replace elements from index 5 to 9 with even numbers
for i in range(5, 10):
 numbers[i] = 2 * (i + 1)
 # Print the modified list
 print("Modified List:", numbers)


# 3. Write a python program to count occurrences of all the elements present in the list.
# - Provide a list.
# - Print all the elements of the list with their counts.
# - Print the list.

my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
 # Create an empty dictionary to store element counts
element_counts = {}
 # Count occurrences of elements in the list
for item in my_list:
 if item in element_counts:
    element_counts[item] += 1
 else:
    element_counts[item] = 1

 # Print elements with their counts
for item, count in element_counts.items():
 print(f"{item}: {count} times")
 print("Original List:", my_list)

#Assignment(Try this yourself)
# 4. Write a python program for List Sorting and Reversing list.
# - Create a list of unsorted numbers.
# - Sort the list in ascending order.
# - Reverse the sorted list.
# - Print the reversed list.

 # Create a list of unsorted numbers
unsorted_list = [4, 2, 9, 1, 5]
 # Sort the list in ascending order
sorted_list = sorted(unsorted_list)

 # Reverse the sorted list
sorted_list.reverse()
print("Reversed List:", sorted_list)

# 5. Write a python program to demonstrate listconcatenation in Python.
# - Provide two lists of names (e.g., boy’s names and girl’s names).
# - Concatenate the two lists to create a combined list of names.
# - Print the combined list.

# Provide two lists of names
boys_names = ["Sahil", "James", "Michael"]
girls_names = ["Emma", "Olivia", "Sophia"]

 # Concatenate the two lists
combined_names = boys_names + girls_names
print("Combined Names:", combined_names)

