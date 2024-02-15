# - Resources to follow :
#   - [Python Documentation - Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
#       - [Real Python - Python Exception Handling](https://realpython.com/courses/working-python-exceptions/)

# 1. Write a Python program that prompts the user to enter two numbers and then performs division. 
# Handle the "ZeroDivisionError" exception if the second number is zero.

try:
 num1 = float(input("Enter the first number: "))
 num2 = float(input("Enter the second number: "))
 result = num1 / num2
 print(f"Result: {result}")
except ZeroDivisionError:
 print("Error: Division by zero is not allowed.")

# 2. Create a Python program that reads a file specified by the user. Handle both "FileNotFoundError" and "PermissionError" exceptions. 
# If the file exists but cannot be opened, Inform the user of the issue.

try:
 filename = input("Enter the file name: ")
 with open(filename, 'r') as file:
    contents = file.read()
    print("File contents:\n", contents)
except FileNotFoundError:
 print(f"Error: File '{filename}' not found.") 
except PermissionError:
 print(f"Error: Permission denied to access'{filename}'.")
except Exception as e:
 print(f"Error: {e}")

#Assignment(Try this yourself)
# 3. Create a program that takes an input number from the user and checks if it's a prime number. 
# Implement the logic inside a function. Use a try-except block to handle any exceptions, and use the else block to print
# whether the number is prime or not.

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
            return True
    try:
        num = int(input("Enter a number: "))
        if is_prime(num):
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")
    except ValueError:
        print("Error: Please enter a valid number.")

# 4. Write a Python program to simulate a simple ATM machine. Create a function that accepts the user's account balance and withdrawal amount. 
# If the withdrawal amount is greater than the account balance, raise a "InsufficientFundsError" exception.

class InsufficientFundsError(Exception):
 pass
 def atm_withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError("Insufficient funds in your account.")
        return balance - amount
    try:
        balance = float(input("Enter your account balance: "))
        withdraw_amount = float(input("Enter withdrawal amount: "))
        new_balance = atm_withdraw(balance, withdraw_amount)
        print(f"Withdrawal successful. New balance: {new_balance}")
    except ValueError:
        print("Error: Please enter valid numbers.")
    except InsufficientFundsError as e:
        print(f"Error: {e}")

#Assignment(Try this yourself)
# 5. Write a program that takes a list of integers from the user and calculates the reciprocal of each number. 
# Handle any exceptions that may occur during the division and continue the loop.

try:
 numbers = [int(x) for x in input("Enter a list of integers: ").split()]
 reciprocals = []
 for num in numbers:
    try:
        reciprocal = 1 / num
        reciprocals.append(reciprocal)
    except ZeroDivisionError:
        reciprocals.append("Undefined")
        print("Reciprocals:", reciprocals)
except ValueError:
    print("Error: Please enter valid integers.")

# 6. Develop a program that reads a file and prints its contents. Handle the "FileNotFoundError" exception. 
# Regardless of whether the file is found or not, use the "finally" block to display a message indicating the end of the program.

try:
 filename = input("Enter the file name: ")
 with open(filename, 'r') as file:
    contents = file.read()
    print("File contents:\n", contents)
except FileNotFoundError:
 print(f"Error: File '{filename}' not found.")
except Exception as e:
 print(f"Error: {e}") 
finally:
 print("End of the program.")

# 7. Create a Python program that performs a series of mathematical operations on two user-input numbers. 
# Handle exceptions such as "ZeroDivisionError" and "ValueError." If any exception occurs, provide a detailed error message.

try:
 num1 = float(input("Enter the first number: "))
 num2 = float(input("Enter the second number: "))
 result = num1 / num2
 print(f"Result: {result}")
except ZeroDivisionError:
 print("Error: Division by zero is not allowed.")
except ValueError:
 print("Error: Please enter valid numbers.")
except Exception as e:
 print(f"Error: {e}")

#Assignment(Try this yourself)
# 8. Write a program that defines a function that opens a specified file and reads its contents. If the file does not exist, 
# the function should raise a "FileNotFoundError." In the main program, handle this exception and print an error message.

def read_file_contents(filename):
 try:
    with open(filename, 'r') as file:
        contents = file.read()
        return contents
 except FileNotFoundError:
    raise FileNotFoundError("Error: The specified file does not exist.")
 except Exception as e:
    print(f"Error: {e}")
 filename = input("Enter the file name: ")
 try:
    file_contents = read_file_contents(filename)
    if file_contents:
        print("File contents:")
        print(file_contents)
 except FileNotFoundError as e:
    print(e)
 except Exception as e:
    print(f"An unexpected error occurred: {e}")

#Assignment(Try this yourself)
# 9. Provide a Python code snippet with a deliberate error (e.g., a syntax error or a logical error)
#  and ask the student to identify and fix the issue using the information provided in the exception message.

try:
 num1 = int(input("Enter the first number: "))
 num2 = int(input("Enter the second number: "))
 result = num1 / num2
 print(f"Result: {result}")
except ZeroDivisionError:
 print("Error: Division by zero is not allowed.")
except ValueError as ve:
 print(f"ValueError: {ve}")

