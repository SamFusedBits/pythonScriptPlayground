# - Resources to follow :
#   - [Real Python - Reading and Writing Files in Python](https://realpython.com/read-write-files-python/)

# 1. WAPP to read content of the file and count how many times letter 'a' comes in a file.

myfile = open("myfile.txt", "r")
contents = myfile.read()
count_a = contents.lower().count('a')
print(f"The letter 'a' appears {count_a} times in the file.")
myfile.close()

# 2. WAPP to read content of a line and display 'I' in place of 'E' while displaying the content of the file,
#    all the other characters should appear as it is.

myfile = open("myfile2.txt", "r")
contents = myfile.read()
content = contents.replace('e', 'I')
print(content)
myfile.close()

#Assignment(Try this yourself)
# 3.Create a Python program that merges the contents of multiple text files into a single file,
# ensuring the lines are sorted in alphabetical order.

myfile1 = open("student.txt","r")
myfile2 = open("data.txt","r")
myfile3 = open("book_backup.txt","r")
myfile4 = open("temp.txt","r")
myfile5 = open("file.txt","w+")
str1 = myfile1.readlines()
str2 = myfile2.readlines()
str3 = myfile3.readlines()
str4 = myfile4.readlines()
str5 =str1+str2+str3+str4
sortedlines = sorted(str5)
myfile5.writelines(sortedlines)
myfile5.close()
myfile = open("file.txt","r")
sorted_lines = myfile.readlines()
for line in sorted_lines:
 print(line,end="")
