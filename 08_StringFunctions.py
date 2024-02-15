# 1. Write a python program to check if an entered string is a palindrome or not?

newstr=input("Enter a string:").lower()
if newstr==newstr[::-1]:
    print("It is a palindrome!")
else:
    print("It is not a palindrome")

# 2. Write a python program to split a given string into lines.

str="Python Lab Assignment 8"
for i in str.split():
    print(i)

#Assignment(Try this yourself)
# 3. Write a python program to remove specific characters from the string. (e.g. removing ‘!’ from the string "Hello World!")

originalstr="Hello World!"
char_to_remove = "!"
rstr=originalstr.replace(char_to_remove, "")
print(originalstr)
print(rstr)

#Assignment(Explore & Try this yourself)
#4. Write a python program to demonstrate more on string function:
# len( ), strip( ), rstrip( ), lstrip( ), find( ), rfind( ), index( ), rindex(), count( ),
# replace( ), split( ), join( ), upper( ), lower( ), swapcase( ), title( ), capitalize( ), startswith(), endswith()

text = " This is a sample text. Hello, universe! "

 #(i) len()
length = len(text)
print(length)

 #(ii) strip()
strip = text.strip()
print(strip)
 
 #(iii) rstrip()
rstrip = text.rstrip()
print(rstrip)
    
 #(iv) lstrip()
lstrip = text.lstrip()
print(lstrip)

 #(v) find()
find = text.find("This")
print(find)

 #(vi) rfind()
rfind = text.rfind("universe")
print(rfind)

 #(vii) index()
index = text.index("Hello")
print(index)

 #(viii) rindex()
rindex = text.rindex("o")
print(rindex)

 #(ix) count()
count = text.count("l")
print(count)

 #(x) replace()
replaced_text = text.replace("universe", "world")
print(text)
print(replaced_text)

 #(xi) split()
split = text.split(",")
print(split)

 #(xii) join()
join = "-".join(split_text)
print(join)

 #(xiii) upper()
upper = text.upper()
print(upper)

 #(xiv) lower()
lower = text.lower()
print(lower)

 #(xv) swapcase()
swapcase = text.swapcase()
print(swapcase)

 #(xvi) title()
title = text.title()
print(title)

 #(xvii) capitalize()
new_text= "this is a capitalized text"
capitalize_text = new_text.capitalize()
print(capitalize_text)

 #(xviii) startswith()
startswith = text.startswith(" ")
print(startswith)

 #(xix) endswith()
endswith = text.endswith("all")
print(endswith)