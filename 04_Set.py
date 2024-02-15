# 1. Write a Python program to find and print the unique elements in a given list.
# - Create a list that contains duplicate elements.
# - Use a set to identify and print the unique elements from the list.

# Create a list with duplicate elements
my_list = [1, 2, 2, 3, 4, 4, 5]
 # Use a set to identify unique elements
unique_elements = set(my_list)
 # Print the unique elements
print("Unique Elements:", unique_elements)

# 2. Write a python program for Set Operations with Two Sets: Consider two sets of numbers.
# - Calculate and print the union of the two sets.
# - Calculate and print the intersection of the two sets.
# - Calculate and print the symmetric difference between the two sets.

# Create two sets of numbers
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
 # Calculate and print the union of the two sets
union_set = set1.union(set2)
print("Union of Sets:", union_set)
 # Calculate and print the intersection of the two sets
intersection_set = set1.intersection(set2)
print("Intersection of Sets:", intersection_set)
 # Calculate and print the symmetric difference between the two sets
symmetric_difference = set1.symmetric_difference(set2)
print("Symmetric Difference of Sets:", symmetric_difference)

#Assignment(Try this yourself)
# 3. Write a python program to Create two lists of items for books in two libraries and identify common books present in both the libraries.
# - Use sets to identify common books and create a new set.
# - Print the set of common items.

 # Create two lists of items for books in two libraries
library1 = {"Database Applications", "Web Technology", "Python", "Artifical Intelligence"}
library2 = {"Python", "Artifical Intelligence", "Presenation skills", "Business Stats"}
 # Use sets to identify common books
common_books = library1.intersection(library2) 
 # Print the set of common items (common books)
print("Common Books:", common_books)


# 4. Write a python program to create a set of unique words in the text, removing punctuation and converting all words to lowercase

def extract_unique_words(text):
 # Define a string of punctuation characters
 punctuation_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

 # Remove punctuation and convert to lowercase
 text = text.lower()
 text = ''.join(char for char in text if char not in punctuation_chars)

 # Split the text into words and create a set of unique words
 words = text.split()
 unique_words = set(words)

 return unique_words
 # Example text
text = "This is a simple example text, with some punctuation. This is a simple example text."
unique_words_set = extract_unique_words(text)
print(unique_words_set)
