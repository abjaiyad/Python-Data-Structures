"""
=====================================================
 PYTHON TUPLES - Notes + Runnable Examples
=====================================================
A tuple is a collection of items (can be different data types) which is:
  - ORDERED       -> items keep their position
  - UNCHANGEABLE  -> immutable: once created, values cannot be changed
  - Written with round brackets ()

Because tuples are immutable, we CANNOT use add, insert or remove on them.
Unlike lists, tuples have very few methods:

  tuple()   -> create an empty tuple
  count()   -> count how many times an item appears in a tuple
  index()   -> find the index of an item in a tuple
  +         -> join two or more tuples and create a NEW tuple

Tip: Run this file in VS Code with the "Run Python File" button (top right).
"""


def section(title):
    """Print a neat heading so the output is easy to read in the terminal."""
    print("\n" + "=" * 55)
    print(f" {title}")
    print("=" * 55)


# -----------------------------------------------------
# 1. CREATING A TUPLE
# -----------------------------------------------------
section("1. Creating a Tuple")

# Empty tuple
empty_tuple = ()
print("Empty tuple (brackets)    :", empty_tuple)

# or using the tuple constructor
empty_tuple = tuple()
print("Empty tuple (constructor) :", empty_tuple)

# Tuple with initial values
tpl = ('item1', 'item2', 'item3')
fruits = ('banana', 'orange', 'mango', 'lemon')
print("tpl   :", tpl)
print("fruits:", fruits)


# -----------------------------------------------------
# 2. TUPLE LENGTH
# -----------------------------------------------------
section("2. Tuple Length")

# len() returns the number of items
tpl = ('item1', 'item2', 'item3')
print("Length of tpl   :", len(tpl))
print("Length of fruits:", len(fruits))


# -----------------------------------------------------
# 3. ACCESSING TUPLE ITEMS
# -----------------------------------------------------
section("3. Accessing Tuple Items")

# 3a. Positive indexing (starts from 0, just like lists)
tpl = ('item1', 'item2', 'item3')
first_item = tpl[0]
second_item = tpl[1]
print("First item :", first_item)
print("Second item:", second_item)

fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index = len(fruits) - 1          # last index = length - 1
last_fruit = fruits[last_index]
print("First fruit :", first_fruit)
print("Second fruit:", second_fruit)
print("Last fruit  :", last_fruit)

# 3b. Negative indexing
# Starts from the END: -1 = last item, -2 = second last, ...
# The negative of the tuple length (-len) refers to the FIRST item.
tpl = ('item1', 'item2', 'item3', 'item4')
first_item = tpl[-4]
second_item = tpl[-3]
print("\nNegative indexing on tpl:")
print("tpl[-4]:", first_item)
print("tpl[-3]:", second_item)

fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[-4]
second_fruit = fruits[-3]
last_fruit = fruits[-1]
print("fruits[-4]:", first_fruit)
print("fruits[-3]:", second_fruit)
print("fruits[-1]:", last_fruit)


# -----------------------------------------------------
# 4. SLICING TUPLES
# -----------------------------------------------------
section("4. Slicing Tuples")

# Slicing returns a NEW tuple.
# Syntax: tuple[start : end]  -> 'end' index is NOT included

# 4a. Range of positive indexes
tpl = ('item1', 'item2', 'item3', 'item4')
all_items = tpl[0:4]            # all items
all_items = tpl[0:]             # all items (end is optional)
middle_two_items = tpl[1:3]     # does not include item at index 3
print("tpl[0:4]:", tpl[0:4])
print("tpl[0:] :", tpl[0:])
print("tpl[1:3]:", middle_two_items)

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:4]        # all items
all_fruits = fruits[0:]         # all items
orange_mango = fruits[1:3]      # does not include item at index 3
orange_to_the_rest = fruits[1:]
print("fruits[1:3]:", orange_mango)
print("fruits[1:] :", orange_to_the_rest)

# 4b. Range of negative indexes
tpl = ('item1', 'item2', 'item3', 'item4')
all_items = tpl[-4:]              # all items
middle_two_items = tpl[-3:-1]     # does not include the item at index -1
print("\ntpl[-4:]  :", all_items)
print("tpl[-3:-1]:", middle_two_items)

fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[-4:]          # all items
orange_mango = fruits[-3:-1]      # does not include the item at index -1
orange_to_the_rest = fruits[-3:]
print("fruits[-4:]  :", all_fruits)
print("fruits[-3:-1]:", orange_mango)
print("fruits[-3:]  :", orange_to_the_rest)


# -----------------------------------------------------
# 5. CHANGING TUPLES TO LISTS
# -----------------------------------------------------
section("5. Changing Tuples to Lists")

# A tuple is immutable. To modify it:
#   tuple -> list -> modify -> tuple
tpl = ('item1', 'item2', 'item3', 'item4')
lst = list(tpl)
print("Tuple converted to list:", lst)

fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)             # tuple -> list
fruits[0] = 'apple'               # lists CAN be changed
print(fruits)                     # ['apple', 'orange', 'mango', 'lemon']

fruits = tuple(fruits)            # list -> tuple
print(fruits)                     # ('apple', 'orange', 'mango', 'lemon')


# -----------------------------------------------------
# 6. CHECKING AN ITEM IN A TUPLE
# -----------------------------------------------------
section("6. Checking an Item in a Tuple")

# `in` returns a boolean (True / False)
tpl = ('item1', 'item2', 'item3', 'item4')
print("'item2' in tpl:", 'item2' in tpl)         # True

fruits = ('banana', 'orange', 'mango', 'lemon')
print("'orange' in fruits:", 'orange' in fruits)  # True
print("'apple' in fruits :", 'apple' in fruits)   # False

# Trying to change a tuple item raises an error
try:
    fruits[0] = 'apple'
except TypeError as error:
    print("Error as expected ->", error)
    # TypeError: 'tuple' object does not support item assignment


# -----------------------------------------------------
# 7. JOINING TUPLES
# -----------------------------------------------------
section("7. Joining Tuples")

# The + operator joins two or more tuples into a NEW tuple
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5', 'item6')
tpl3 = tpl1 + tpl2
print("tpl1 + tpl2:", tpl3)

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
print("fruits + vegetables:", fruits_and_vegetables)


# -----------------------------------------------------
# 8. TUPLE METHODS: count() AND index()
# -----------------------------------------------------
section("8. Tuple Methods: count() and index()")

# count() -> how many times an item appears
# index() -> position of the FIRST matching item
letters = ('a', 'b', 'a', 'c', 'a')
print("letters.count('a'):", letters.count('a'))   # 3
print("letters.index('c'):", letters.index('c'))   # 3
print("letters.index('a'):", letters.index('a'))   # 0 (first match)


# -----------------------------------------------------
# 9. DELETING TUPLES
# -----------------------------------------------------
section("9. Deleting Tuples")

# We CANNOT remove a single item from a tuple,
# but we CAN delete the whole tuple using del.
tpl1 = ('item1', 'item2', 'item3')
del tpl1

fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits

try:
    print(fruits)
except NameError as error:
    print("Tuple deleted! Error as expected ->", error)


# -----------------------------------------------------
# QUICK CHEAT SHEET
# -----------------------------------------------------
"""
Operation            Code
------------------   ------------------------------
Empty tuple          () or tuple()
Length               len(t)
Positive index       t[0], t[1], ...
Negative index       t[-1] (last), t[-len(t)] (first)
Slice                t[start:end]   (end not included)
Tuple -> list        list(t)
List -> tuple        tuple(lst)
Membership           x in t
Join tuples          t1 + t2
Count an item        t.count(x)
Find an index        t.index(x)
Delete tuple         del t
"""
