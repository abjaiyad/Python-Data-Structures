"""
=====================================================
 PYTHON LISTS - Notes + Runnable Examples
=====================================================
There are FOUR collection data types in Python:

  List       -> ordered, changeable (mutable). Allows duplicates.
  Tuple      -> ordered, unchangeable (immutable). Allows duplicates.
  Set        -> unordered, un-indexed, items can't be changed but new items
                CAN be added. No duplicates.
  Dictionary -> unordered, changeable, indexed (by keys). No duplicate keys.

A LIST is a collection of items (can be different data types) that is
ordered and modifiable. A list can be empty or hold mixed data types.

Tip: Run this file in VS Code with the "Run Python File" button (top right).
"""


def section(title):
    """Print a neat heading so the output is easy to read in the terminal."""
    print("\n" + "=" * 55)
    print(f" {title}")
    print("=" * 55)


# -----------------------------------------------------
# 1. HOW TO CREATE A LIST
# -----------------------------------------------------
section("1. How to Create a List")

# Way 1: using the list() built-in function
lst = list()
empty_list = list()              # an empty list, no items
print("Empty list (list()):", empty_list, "| length:", len(empty_list))   # 0

# Way 2: using square brackets []
lst = []
empty_list = []                  # an empty list, no items
print("Empty list ([])    :", empty_list, "| length:", len(empty_list))   # 0

# Lists with initial values. Use len() to find the length of a list.
fruits = ['banana', 'orange', 'mango', 'lemon']                       # fruits
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']       # vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']               # animal products
web_techs = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongoDB']  # web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']     # countries

# Print the lists and their lengths
print('\nFruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:', animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Countries:', countries)
print('Number of countries:', len(countries))

# Lists can hold items of DIFFERENT data types
lst = ['Asabeneh', 250, True, {'country': 'Finland', 'city': 'Helsinki'}]
print('\nMixed data types:', lst)


# -----------------------------------------------------
# 2. ACCESSING ITEMS - POSITIVE INDEXING
# -----------------------------------------------------
section("2. Accessing Items - Positive Indexing")

# A list index starts from 0
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0]          # first item using its index
print(first_fruit)               # banana
second_fruit = fruits[1]
print(second_fruit)              # orange
last_fruit = fruits[3]
print(last_fruit)                # lemon

# Last index = length - 1
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
print("Using last_index:", last_fruit)   # lemon


# -----------------------------------------------------
# 3. ACCESSING ITEMS - NEGATIVE INDEXING
# -----------------------------------------------------
section("3. Accessing Items - Negative Indexing")

# Start from the END: -1 = last item, -2 = second last, ...
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[-4]
last_fruit = fruits[-1]
second_last = fruits[-2]
print(first_fruit)      # banana
print(last_fruit)       # lemon
print(second_last)      # mango


# -----------------------------------------------------
# 4. UNPACKING LIST ITEMS
# -----------------------------------------------------
section("4. Unpacking List Items")

# The *rest variable collects all the remaining items into a list
lst = ['item1', 'item2', 'item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']

# First example
print("\n-- First example --")
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime', 'apple']
first_fruit, second_fruit, third_fruit, *rest = fruits
print(first_fruit)    # banana
print(second_fruit)   # orange
print(third_fruit)    # mango
print(rest)           # ['lemon', 'lime', 'apple']

# Second example: *rest in the MIDDLE
print("\n-- Second example --")
first, second, third, *rest, tenth = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(first)          # 1
print(second)         # 2
print(third)          # 3
print(rest)           # [4, 5, 6, 7, 8, 9]
print(tenth)          # 10

# Third example
print("\n-- Third example --")
countries = ['Germany', 'France', 'Belgium', 'Sweden', 'Denmark',
             'Finland', 'Norway', 'Iceland', 'Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)             # Germany
print(fr)             # France
print(bg)             # Belgium
print(sw)             # Sweden
print(scandic)        # ['Denmark', 'Finland', 'Norway', 'Iceland']
print(es)             # Estonia


# -----------------------------------------------------
# 5. SLICING ITEMS FROM A LIST
# -----------------------------------------------------
section("5. Slicing Items from a List")

# Syntax: list[start : end : step]   -> returns a NEW list
# Defaults: start = 0, end = end of list, step = 1
# The 'end' index is NOT included.

# 5a. Positive indexing
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4]            # all the fruits
all_fruits = fruits[0:]             # same result: no end = take all the rest
orange_and_mango = fruits[1:3]      # the END index (3) is not included
orange_mango_lemon = fruits[1:]
every_second_fruit = fruits[::2]    # step = 2 -> every 2nd item
print("fruits[0:4]:", fruits[0:4])
print("fruits[0:]:", all_fruits)
print("fruits[1:3]:", orange_and_mango)
print("fruits[1:]:", orange_mango_lemon)
print("fruits[::2]:", every_second_fruit)   # ['banana', 'mango']

# 5b. Negative indexing
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:]            # all the fruits
orange_and_mango = fruits[-3:-1]    # the END index (-1) is not included
orange_mango_lemon = fruits[-3:]    # from -3 to the end
reverse_fruits = fruits[::-1]       # negative step = reverse order
print("\nfruits[-4:]:", all_fruits)
print("fruits[-3:-1]:", orange_and_mango)       # ['orange', 'mango']
print("fruits[-3:]:", orange_mango_lemon)       # ['orange', 'mango', 'lemon']
print("fruits[::-1]:", reverse_fruits)          # ['lemon', 'mango', 'orange', 'banana']


# -----------------------------------------------------
# 6. MODIFYING LISTS
# -----------------------------------------------------
section("6. Modifying Lists")

# A list is mutable, so we can change items by their index
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print(fruits)       # ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'apple'
print(fruits)       # ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)       # ['avocado', 'apple', 'mango', 'lime']


# -----------------------------------------------------
# 7. CHECKING ITEMS IN A LIST
# -----------------------------------------------------
section("7. Checking Items in a List")

# Use the `in` operator -> returns True or False
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)   # True
does_exist = 'lime' in fruits
print(does_exist)   # False


# -----------------------------------------------------
# 8. ADDING ITEMS TO A LIST - append()
# -----------------------------------------------------
section("8. Adding Items - append()")

# append() adds an item to the END of the list
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)       # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime')
print(fruits)       # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']


# -----------------------------------------------------
# 9. INSERTING ITEMS INTO A LIST - insert()
# -----------------------------------------------------
section("9. Inserting Items - insert()")

# insert(index, item) adds ONE item at a given index.
# Other items are shifted to the right.
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple')       # insert apple between orange and mango
print(fruits)       # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')
print(fruits)       # ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']


# -----------------------------------------------------
# 10. REMOVING ITEMS - remove()
# -----------------------------------------------------
section("10. Removing Items - remove()")

# remove(item) removes the FIRST occurrence of the item
fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana')
print(fruits)       # ['orange', 'mango', 'lemon', 'banana']
fruits.remove('lemon')
print(fruits)       # ['orange', 'mango', 'banana']


# -----------------------------------------------------
# 11. REMOVING ITEMS - pop()
# -----------------------------------------------------
section("11. Removing Items - pop()")

# pop() removes the item at the given index,
# or the LAST item if no index is given.
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()        # removes the last item
print(fruits)       # ['banana', 'orange', 'mango']

fruits.pop(0)       # removes the item at index 0
print(fruits)       # ['orange', 'mango']


# -----------------------------------------------------
# 12. REMOVING ITEMS - del
# -----------------------------------------------------
section("12. Removing Items - del")

# del removes an index, a range of indexes, or the whole list
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)       # ['orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[1]
print(fruits)       # ['orange', 'lemon', 'kiwi', 'lime']
del fruits[1:3]     # deletes index 1 and 2 (index 3 is NOT deleted)
print(fruits)       # ['orange', 'lime']

del fruits          # deletes the list completely
try:
    print(fruits)
except NameError as error:
    print("List deleted! Error as expected ->", error)   # name 'fruits' is not defined


# -----------------------------------------------------
# 13. CLEARING LIST ITEMS - clear()
# -----------------------------------------------------
section("13. Clearing List Items - clear()")

# clear() empties the list but keeps the list itself
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)       # []


# -----------------------------------------------------
# 14. COPYING A LIST
# -----------------------------------------------------
section("14. Copying a List")

# DANGER: list2 = list1 does NOT make a copy.
# list2 is just another name (reference) for the SAME list,
# so changing list2 also changes list1.
list1 = ['a', 'b', 'c']
list2 = list1
list2.append('d')
print("list1 after changing list2:", list1)   # ['a', 'b', 'c', 'd']  <- changed!

# SAFE: copy() makes a separate, independent copy
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
fruits_copy.append('apple')
print("fruits     :", fruits)         # unchanged
print("fruits_copy:", fruits_copy)    # has apple


# -----------------------------------------------------
# 15. JOINING LISTS
# -----------------------------------------------------
section("15. Joining Lists")

# 15a. Plus operator (+) -> creates a NEW list
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5, -4, -3, -2, -1]
integers = negative_numbers + zero + positive_numbers
print(integers)     # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

# 15b. extend() -> adds the items of one list INTO the original list
print("\n-- extend() --")
list1 = ['item1', 'item2']
list2 = ['item3', 'item4', 'item5']
list1.extend(list2)
print(list1)        # ['item1', 'item2', 'item3', 'item4', 'item5']

num1 = [0, 1, 2, 3]
num2 = [4, 5, 6]
num1.extend(num2)
print('Numbers:', num1)             # [0, 1, 2, 3, 4, 5, 6]

negative_numbers = [-5, -4, -3, -2, -1]
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers)   # [-5, ..., -1, 0, 1, ..., 5]

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits.extend(vegetables)
print('Fruits and vegetables:', fruits)


# -----------------------------------------------------
# 16. COUNTING ITEMS IN A LIST - count()
# -----------------------------------------------------
section("16. Counting Items - count()")

# count(item) -> how many times the item appears
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           # 3


# -----------------------------------------------------
# 17. FINDING THE INDEX OF AN ITEM - index()
# -----------------------------------------------------
section("17. Finding Index - index()")

# index(item) -> index of the FIRST occurrence
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))           # 2 (the first occurrence)


# -----------------------------------------------------
# 18. REVERSING A LIST - reverse()
# -----------------------------------------------------
section("18. Reversing a List - reverse()")

# reverse() flips the order and modifies the ORIGINAL list
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits)       # ['lemon', 'mango', 'orange', 'banana']
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages)         # [24, 25, 24, 26, 25, 24, 19, 22]


# -----------------------------------------------------
# 19. SORTING LIST ITEMS
# -----------------------------------------------------
section("19. Sorting List Items")

# sort()   -> sorts the ORIGINAL list (modifies it)
# sorted() -> returns a NEW sorted list (original is unchanged)
# reverse=True -> descending order

# 19a. sort()
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)       # ['banana', 'lemon', 'mango', 'orange']
fruits.sort(reverse=True)
print(fruits)       # ['orange', 'mango', 'lemon', 'banana']

ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages)         # [19, 22, 24, 24, 24, 25, 25, 26]
ages.sort(reverse=True)
print(ages)         # [26, 25, 25, 24, 24, 24, 22, 19]

# 19b. sorted()
print("\n-- sorted() --")
fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits))       # ['banana', 'lemon', 'mango', 'orange']
print("Original unchanged:", fruits)

# Reverse order
fruits = sorted(fruits, reverse=True)
print(fruits)       # ['orange', 'mango', 'lemon', 'banana']


# -----------------------------------------------------
# QUICK CHEAT SHEET
# -----------------------------------------------------
"""
Operation             Code
-------------------   ---------------------------------
Empty list            [] or list()
Length                len(lst)
Access item           lst[0], lst[-1]
Unpack                a, b, *rest = lst
Slice                 lst[start:end:step]
Reverse copy          lst[::-1]
Change item           lst[0] = 'new'
Membership            x in lst
Add to end            lst.append(x)
Insert at index       lst.insert(i, x)
Remove by value       lst.remove(x)
Remove by index       lst.pop(i) / del lst[i]
Empty the list        lst.clear()
Delete the list       del lst
Copy                  lst.copy()
Join                  a + b   /   a.extend(b)
Count                 lst.count(x)
Find index            lst.index(x)
Reverse in place      lst.reverse()
Sort in place         lst.sort(reverse=False)
Sorted new list       sorted(lst, reverse=False)
"""
