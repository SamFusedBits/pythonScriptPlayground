# 1. Write a Python program that takes two strings as input and concatenates them. Ensure thatthe final string is in uppercase. 
# Calculate and print the length of a user-entered string.
# Remove all leading and trailing spaces from a given string.

str1=input("Enter the first string:")
str2=input("Enter the second string:") 

 #Concatenating both the strings
cstr=(str1+str2).upper()
print(cstr)
lstr=len(cstr)
print("Length of concatenated string:",lstr)
rstr=str1.strip()
print("Removed leading/trailing spaces:",rstr)

# 2. a. Write a program to find and print the index of the first occurrence of a substring in each string. 
#    b. Create a Python function that takes a sentence as input and replaces all occurrences of a specified word with a user-defined word.

#(a)
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

sstr = input("Enter a substring to search for: ")
index1= str1.find(sstr)
index2 = str2.find(sstr)
print(f"First occurrence of a substring in the first string is at index:", index1)
print(f"First occurrence of a substring in the second string is at index:", index2)

#(b)
text = input("Enter a sentence: ")
word = input("Enter the word to replace: ")
new_word = input("Enter the new word: ")
modified_sentence = text.replace(word, new_word)
print("Modified Sentence:", modified_sentence)

#Assignment(Try this yourself)
# 3. a. Write a Python function that extracts the domain name from an email address using string slicing.
#    b. Given a list of words separated by spaces, write a program to split the input into individual words and count the number of words.

#(a)
email_addr= input("Enter an email address: ")
index = email_addr.index('@')
domain = email_addr[index + 1:]
print("Domain name:", domain)

# (b) 
str = input("Enter a list of words separated by spaces: ")
words = str.split()
print(words)
count = len(words)
print("Number of words:", count)

#Assignment(Try this yourself)
# 4. Create a Python program that accepts a user's name and age, and then prints a formatted message like "My name is [name] and I am
# [age] years old". Format a given string to title case, and then capitalize the first character of the result.

name = input("Enter your name: ")
age = input("Enter your age: ")
message = f"my name is {name} and i am {age} years old."
cmsg = message.capitalize()
print("Capitalized message:",cmsg)

# 5. Write a Python program to count the number of times a specified character appears in a given string. 
# Implement a function that searches for all occurrences of a specified word in a paragraph and counts them.

sample = "This is a sample string."
ccount = "s"
count = sample.count(ccount)
print(f"The character '{ccount}' appears {count} times in the string.")
paragraph = "This is a python lab. Based on string operations"
wsearch = "lab"
wcount = paragraph.lower().count(wsearch.lower())
print(f"The word '{wsearch}' appears {wcount} times in the paragraph.")


# 6. a) Develop a program that reverses a given string without using string slicing.
# b) Create a Python function that accepts a sentence and removes all punctuation marks from it.

 #(a) 
str = "Hello, universe!"
rstr = "".join(reversed(str))
print("Reversed string:", rstr)

 #(b) 
a=input("enter a string : ")
print("The original string is : ",a)
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
for i in a:
    if i in punc:
        a = a.replace(i, "")
        print("The string after punctuation filter : ",a)

#Assignment(Try this yourself)
# 7. a) Write a Python program that takes a list of words and joins them into a single string with a comma and space as the delimiter.
#    b) Develop a program that reads a paragraph of text and splits it into sentences based on period (.) as the delimiter.

 #(a)
words = ["apple", "banana", "cherry"]
result = ", ".join(words)
print("Before join:",words)
print("After join:", result)

 #(b)
paragraph = "This is a paragraph. With some text"
sentences = paragraph.split(". ")
print("Splitted sentences:", sentences)

# 8. a) Create a Python function that accepts a string and checks whether it starts with an uppercase letter.
#    b) Implement a program that checks if a given string ends with a specific suffix.

 #(a)
str = input("Enter the string:")
if str[0].isupper(): 
 print("string starts with uppercase")
else:
 print("does not starts with uppercase")

#(b)
word = input("Enter any word")
end_word = input("Enter end word to check")
if word.endswith(end_word):
 print("ends with this word")
else:
 print("does not ends with this word")


# 9. a) Write a program that removes all leading and trailing zeros from a user-entered string of numbers.
#    b) Develop a function that strips a given string of a specific character from both ends.

 #(a)
num = input("Enter a string of numbers: ")
 # Remove leading zeros
while num.startswith('0'):
 num = num[1:]
 # Remove trailing zeros
while num.endswith('0'):
 num = num[:-1]
 print("Result:", num)

 #(b)
str = input("Enter a string: ")
char = input("Enter a character to remove: ")
while str.startswith(char):
 str = str[1:]
while str.endswith(char):
 str = str[:-1]
 print("Result:", str) 

#Assignment(Try this yourself)
# 10. Compare two strings entered by the user and determine if they are equal. 
# Find the index of the first occurrence of a user-specified character in a given string.

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
if str1 == str2:
 print("Strings are equal.")
else:
 print("Strings are not equal.")
 char = input("Enter a character to find in the string: ")
if char in str1:
 index = str1.index(char)
 print(f"The first occurrence of '{char}' in the first string is at index {index}.")
else:
 print(f"'{char}' not found in the first string.")