"""
=====================================================
 PYTHON SETS - Notes + Runnable Examples
=====================================================
A set is a collection of UNORDERED, UN-INDEXED and DISTINCT (unique) items.

Python sets follow the same idea as sets in school Mathematics:
you can find union, intersection, difference, symmetric difference,
subset, superset and disjoint sets.

Tip: Run this file in VS Code with the "Run Python File" button (top right).
"""


def section(title):
    """Print a neat heading so the output is easy to read in the terminal."""
    print("\n" + "=" * 55)
    print(f" {title}")
    print("=" * 55)


# -----------------------------------------------------
# 1. CREATING A SET
# -----------------------------------------------------
section("1. Creating a Set")

# Empty set -> use set(). NOTE: {} creates an empty DICTIONARY, not a set!
st = set()
print("Empty set:", st, "| type:", type(st))
print("Empty {}  :", {}, "| type:", type({}))

# Set with initial items
st = {'item1', 'item2', 'item3', 'item4'}
print("Set with items:", st)

# Example
fruits = {'banana', 'orange', 'mango', 'lemon'}
print("Fruits:", fruits)


# -----------------------------------------------------
# 2. GETTING A SET'S LENGTH
# -----------------------------------------------------
section("2. Getting Set's Length")

# len() returns the number of items in the set
print("Length of st    :", len(st))
print("Length of fruits:", len(fruits))


# -----------------------------------------------------
# 3. ACCESSING ITEMS IN A SET
# -----------------------------------------------------
section("3. Accessing Items in a Set")

# Sets have no index, so st[0] will NOT work.
# We use loops to access items (covered in the loops section).
for fruit in fruits:
    print("Fruit:", fruit)


# -----------------------------------------------------
# 4. CHECKING AN ITEM
# -----------------------------------------------------
section("4. Checking an Item")

# Use the `in` membership operator
print("Does set st contain item3? ", 'item3' in st)   # True
print("Is mango in fruits?        ", 'mango' in fruits)  # True
print("Is apple in fruits?        ", 'apple' in fruits)  # False


# -----------------------------------------------------
# 5. ADDING ITEMS TO A SET
# -----------------------------------------------------
section("5. Adding Items to a Set")

# Once a set is created we cannot CHANGE its items,
# but we CAN add new items.

# 5a. Add ONE item using add()
st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')
print("After add():", st)

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')
print("Fruits after add('lime'):", fruits)

# 5b. Add MULTIPLE items using update()
# update() accepts any iterable (list, tuple, set...)
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5', 'item6', 'item7'])
print("After update() with list:", st)

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage', 'onion', 'carrot')  # a tuple
fruits.update(vegetables)
print("Fruits after update(vegetables):", fruits)


# -----------------------------------------------------
# 6. REMOVING ITEMS FROM A SET
# -----------------------------------------------------
section("6. Removing Items from a Set")

# remove() -> raises KeyError if the item is NOT found
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')
print("After remove('item2'):", st)

# Safe way: check first...
if 'item9' in st:
    st.remove('item9')

# ...or use discard(), which never raises an error
st.discard('item9')   # no error even though item9 does not exist
print("After discard('item9'):", st)

# pop() -> removes a RANDOM item and returns it
fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop()
print("Removed item:", removed_item)
print("Fruits left :", fruits)


# -----------------------------------------------------
# 7. CLEARING ITEMS IN A SET
# -----------------------------------------------------
section("7. Clearing Items in a Set")

# clear() empties the set but keeps the set itself
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits)   # set()


# -----------------------------------------------------
# 8. DELETING A SET
# -----------------------------------------------------
section("8. Deleting a Set")

# del removes the set variable completely
fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits

try:
    print(fruits)
except NameError as error:
    print("Set deleted! Error as expected ->", error)


# -----------------------------------------------------
# 9. CONVERTING LIST TO SET
# -----------------------------------------------------
section("9. Converting List to Set")

# Converting a list to a set removes duplicates.
# Only unique items are kept (order is random).
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)
print("List:", lst)
print("Set :", st)

fruits = ['banana', 'orange', 'mango', 'lemon', 'orange', 'banana']
fruits = set(fruits)
print("Unique fruits:", fruits)

# And back from set to list
print("Back to list:", list(fruits))


# -----------------------------------------------------
# 10. JOINING SETS
# -----------------------------------------------------
section("10. Joining Sets")

# Two ways: union() / | (returns a NEW set)
#           update()     (changes the ORIGINAL set)

# 10a. union() -> returns a new set
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)      # same as: st3 = st1 | st2
print("st1.union(st2):", st3)

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage', 'onion', 'carrot'}
print("fruits.union(vegetables):", fruits.union(vegetables))
print("fruits | vegetables     :", fruits | vegetables)

# 10b. update() -> inserts one set INTO another set
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2)           # st2 contents are added to st1
print("st1 after update(st2):", st1)

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage', 'onion', 'carrot'}
fruits.update(vegetables)
print("fruits after update(vegetables):", fruits)


# -----------------------------------------------------
# 11. FINDING INTERSECTION ITEMS
# -----------------------------------------------------
section("11. Finding Intersection Items")

# Intersection = items that are in BOTH sets. Use intersection() or &
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
print("st1.intersection(st2):", st1.intersection(st2))   # {'item3', 'item2'}
print("st1 & st2            :", st1 & st2)

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print("whole ∩ even:", whole_numbers.intersection(even_numbers))

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
print("python ∩ dragon:", python.intersection(dragon))   # {'o', 'n'}
print("python & dragon:", python & dragon)


# -----------------------------------------------------
# 12. CHECKING SUBSET AND SUPERSET
# -----------------------------------------------------
section("12. Checking Subset and Superset")

# Subset   : issubset()    -> all items of A are inside B
# Superset : issuperset()  -> A contains all items of B
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print("st2.issubset(st1)  :", st2.issubset(st1))     # True
print("st1.issuperset(st2):", st1.issuperset(st2))   # True

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print("whole.issubset(even)  :", whole_numbers.issubset(even_numbers))    # False (it is a superset)
print("whole.issuperset(even):", whole_numbers.issuperset(even_numbers))  # True

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
print("python.issubset(dragon):", python.issubset(dragon))   # False


# -----------------------------------------------------
# 13. CHECKING THE DIFFERENCE BETWEEN TWO SETS
# -----------------------------------------------------
section("13. Difference Between Two Sets")

# A.difference(B) or A - B  -> items in A that are NOT in B
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print("st2.difference(st1):", st2.difference(st1))   # set()
print("st1.difference(st2):", st1.difference(st2))   # {'item1', 'item4'}

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print("whole - even:", whole_numbers.difference(even_numbers))   # {1, 3, 5, 7, 9}

python = {'p', 'y', 't', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
print("python - dragon:", python.difference(dragon))   # {'p', 'y', 't'}
print("dragon - python:", dragon.difference(python))   # {'d', 'r', 'a', 'g'}
# Note: the result order is random, because sets are unordered.


# -----------------------------------------------------
# 14. FINDING SYMMETRIC DIFFERENCE BETWEEN TWO SETS
# -----------------------------------------------------
section("14. Symmetric Difference")

# Returns all items from both sets EXCEPT the ones present in both.
# Mathematically: (A \ B) ∪ (B \ A)   | Short form: A ^ B
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print("st2.symmetric_difference(st1):", st2.symmetric_difference(st1))  # {'item1', 'item4'}
print("st2 ^ st1                    :", st2 ^ st1)

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
print("whole ^ some:", whole_numbers.symmetric_difference(some_numbers))  # {0, 6, 7, 8, 9, 10}

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
print("python ^ dragon:", python.symmetric_difference(dragon))


# -----------------------------------------------------
# 15. DISJOINT SETS
# -----------------------------------------------------
section("15. Disjoint Sets")

# Two sets with NO common item are called disjoint sets.
# Check using isdisjoint()
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print("st2.isdisjoint(st1):", st2.isdisjoint(st1))   # False

even_numbers = {0, 2, 4, 6, 8}
odd_numbers = {1, 3, 5, 7, 9}
print("even.isdisjoint(odd):", even_numbers.isdisjoint(odd_numbers))   # True, no common item

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
print("python.isdisjoint(dragon):", python.isdisjoint(dragon))   # False, common: {'o', 'n'}


# -----------------------------------------------------
# QUICK CHEAT SHEET
# -----------------------------------------------------
"""
Operation               Method                        Operator
---------------------   ---------------------------   --------
Create empty set        set()                         -
Length                  len(s)                        -
Membership              -                             x in s
Add one item            s.add(x)                      -
Add many items          s.update(iterable)            -
Remove (error if no)    s.remove(x)                   -
Remove (no error)       s.discard(x)                  -
Remove random item      s.pop()                       -
Empty the set           s.clear()                     -
Delete the set          -                             del s
Union                   a.union(b)                    a | b
Intersection            a.intersection(b)             a & b
Difference              a.difference(b)               a - b
Symmetric difference    a.symmetric_difference(b)     a ^ b
Subset / Superset       a.issubset(b) / a.issuperset(b)
Disjoint                a.isdisjoint(b)               -
"""