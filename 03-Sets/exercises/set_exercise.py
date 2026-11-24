# sets
from multiprocessing.reduction import duplicate


it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Q) Find the length of the set it_companies
print("Length of it_companies:", len(it_companies))

# Q) Add 'Twitter' to it_companies
it_companies.add("Twitter")

# Q) Insert multiple IT companies at once to the set it_companies
it_companies.update(["LinkedIn", "Snapchat"])

# Q) Remove one of the companies from the set it_companies
it_companies.remove("Facebook")

# Q) What is the difference between remove and discard
# `remove` raises a KeyError if the item is not found
# `discard` does not raise an error if the item is not found
it_companies.discard("NonExistentCompany")

# Q) Join A and B
print("A.union(B):", A.union(B))

# Q) Find A intersection B
print("A.intersection(B):", A.intersection(B))

# Q) Is A subset of B
print("A.issubset(B):", A.issubset(B))

# Q) Are A and B disjoint sets
print("A.isdisjoint(B):", A.isdisjoint(B))

# Q) Join A with B and B with A
print("A | B:", A | B)
print("B | A:", B | A)

# Q) What is the symmetric difference between A and B
print("A ^ B:", A ^ B)

# Q) Delete the sets completely
del A
del B

# Q) Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
print("Length of age list:", len(age))
print("Length of age set:", len(age_set))

# Q) Explain the difference between the following data types: string, list, tuple and set
'''
Answer:

string: An immutable sequence of characters, used to represent text.
list: An ordered, mutable collection of items, which can contain elements of different data types.
tuple: An ordered, immutable collection of items, which can also contain elements of different data types.
set: An unordered collection of unique items, which is mutable and does not allow duplicate elements.
'''

'''
Q) I am a teacher and I love to inspire and teach people.
   How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
'''

sentence = "I am a teacher and I love to inspire and teach people."
# Remove punctuation and convert to lowercase
sentence = sentence.replace(".", "").lower()
print("Processed sentence:", sentence)
# Split the sentence into words and convert to a set to get unique words
unique_words = set(sentence.split())
print("Unique words:", unique_words)
# Print the number of unique words
print("Number of unique words:", len(unique_words))