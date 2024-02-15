# - Resources to follow :
#  - [Python Documentation - Break and Continue Statements](https://docs.python.org/3/tutorial/controlflow.html)

# 1. Write a python program to find the first even number and print.

for num in range(1, 101):
 if num % 2 == 0:
    print("First Even Number:", num)
    break

# 2. Write a python program to skip printing numbers divisible by 3 within a for loop.

for num in range(1, 11):
 if num % 3 == 0:
    continue
    print(num)

# 3. Write a python program to terminate a while loop when the user enters a specific input (e.g.,"exit").

while True:
 user_input = input("Enter 'exit' to terminate: ")
 if user_input.lower() == "exit":
    break

# 4. Write a python program to skip specific values (e.g., negative numbers) when iterating through a list.

numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9, 10]
for num in numbers:
 if num < 0:
    continue
    print(num)

# 5. Write a python program to find and print all prime numbers from 1 to 50. Use a for loop and the break statement to optimize the search for prime numbers.

for num in range(1, 51):
 if num < 2:
    continue
 for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        break
    else:
        print("Prime Number:", num)

# 6. Write a python program that takes a list of integers and prints all positive numbers,
# skipping negative ones using the continue statement.

numbers = [-1, 2, -3, 4, -5, 6, -7, 8, 9, 10]
for num in numbers:
    if num < 0:
        continue
        print("Positive Number:", num)

# 7. Write a python program that asks the user to enter a password. If the password contains at least one uppercase letter, one lowercase letter,
# one digit, and is at least 8 characters long, print "Password accepted." Otherwise, print an appropriate message and continue asking for a password until a valid one is entered.

while True:
 password = input("Enter a password: ")
 if any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char.isdigit() for char in password) and len(password) >= 8:
    print("Password accepted.")
    break
 else:
    print("Invalid password. Please try again.")

# 8. Write a python program that takes a list of numbers and a sum limit. Print the numbers in the list one by one until their sum exceeds the limit,
# then terminate the loop using the break statement.

numbers = [10, 20, 30, 40, 50, 60]
sum_limit = 70
current_sum = 0
for num in numbers:
 if current_sum + num > sum_limit:
    break
current_sum += num
print(num)

# 9. Write a python program that takes a list of numbers and prints unique values (skipping duplicates) using the continue statement.

numbers = [1, 2, 2, 3, 3, 4, 4, 5]
flowers = set()
for num in numbers:
 if num in flowers:
    continue
    flowers.add(num)
    print("Unique Value:", num)
