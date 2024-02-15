# - Resources to follow :
  # - [GeeksforGeeks - Python Switch Case](https://www.geeksforgeeks.org/switch-case-in-python-replacement/)
  #     - [Real Python - Replacements for Switch/Case Statements](https://realpython.com/courses/cool-new-features-python-38/)

# 1. Write a python program to implement switch cases using a dictionary that maps cases to function and take input from the user for case selection.

def case1():
 print("Case 1 is selected.")
def case2():
 print("Case 2 is selected.")
def case3():
 print("Case 3 is selected.")
switch = {
 1:case1,
 2:case2,
 3:case3,
}
try:
 selected_case=int(input("Enter a case(1,2,or3):"))
 selected_function = switch.get(selected_case)
 if selected_function:
  selected_function()
 else:
  print("Invalid Case.")
except ValueError:
 print("Invalid input. Please enter a number(1,2,or3).")

#Assignment(Try this yourself)
# 2. Write a python program that allows user to manage a to do list the program should display a menu with the following action
# - Add task to the list
# - Remove task from the list
# - Display the list

def add_task(todo_list):
 task = input("Enter a task: ")
 todo_list.append(task)
 print("Task added successfully!")
def remove_task(todo_list):
 if not todo_list:
  print("The to-do list is empty.")
 return
 print("To-Do List:")
 for i, task in enumerate(todo_list):
  print(f"{i + 1}. {task}")
 try:
  task_index = int(input("Enter the task number to remove: ")) - 1
  if 0 <= task_index < len(todo_list):
   removed_task = todo_list.pop(task_index)
   print(f"'{removed_task}' has been removed from the list.")
  else:
   print("Invalid task number.")
 except ValueError:
   print("Invalid input. Please enter a valid task number.")
def display_list(todo_list):
 if not todo_list:
  print("The to-do list is empty.")
 else:
  print("To-Do List:")
 for i, task in enumerate(todo_list):
  print(f"{i + 1}. {task}")
def sort_list(todo_list):
 todo_list.sort()
 print("To-Do List sorted successfully!")
def main():
 todo_list = []
 while True:
  print("\nMenu:")
  print("1. Add task to the list")
  print("2. Remove task from the list")
  print("3. Display the list")
  print("4. Sort the list")
  print("5. Quit")
 choice = input("Enter your choice (1/2/3/4/5): ")
 if choice == '1':
  add_task(todo_list)
 elif choice == '2':
  remove_task(todo_list)
 elif choice == '3':
  display_list(todo_list)
 elif choice == '4':
  sort_list(todo_list)
 elif choice == '5':
  print("Goodbye!")
  break
 else:
  print("Invalid choice. Please select a valid option (1/2/3/4/5).")
main()


