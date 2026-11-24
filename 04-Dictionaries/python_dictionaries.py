"""
=====================================================
 PYTHON DICTIONARIES - Notes + Runnable Examples
=====================================================
A dictionary is a collection of paired (key: value) data that is
modifiable (mutable).

  - Created with curly brackets {} or the dict() built-in function
  - Items are accessed by KEY, not by index
  - Keys must be unique
  - Note: the original notes call dictionaries "unordered". In Python 3.7+
    a dictionary remembers the order in which items were inserted, but you
    still cannot access items by position.

Tip: Run this file in VS Code with the "Run Python File" button (top right).
"""


def section(title):
    """Print a neat heading so the output is easy to read in the terminal."""
    print("\n" + "=" * 55)
    print(f" {title}")
    print("=" * 55)


def make_person():
    """Return a fresh copy of the sample dictionary used in the examples.

    Using a function means every section starts with the same clean data,
    even after earlier sections have modified or deleted items.
    """
    return {
        'first_name': 'Asabeneh',
        'last_name': 'Yetayeh',
        'age': 250,
        'country': 'Finland',
        'is_married': True,
        'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
        'address': {
            'street': 'Space street',
            'zipcode': '02210'
        }
    }


# -----------------------------------------------------
# 1. CREATING A DICTIONARY
# -----------------------------------------------------
section("1. Creating a Dictionary")

# Empty dictionary: curly brackets or dict()
empty_dict = {}
empty_dict2 = dict()
print("Empty dictionary:", empty_dict, empty_dict2)

# Dictionary with data values
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
print("dct:", dct)

# A bigger example
person = make_person()
print("\nperson:", person)

# A value can be ANY data type: string, number, boolean,
# list, tuple, set or even another dictionary.


# -----------------------------------------------------
# 2. DICTIONARY LENGTH
# -----------------------------------------------------
section("2. Dictionary Length")

# len() counts the number of 'key: value' pairs
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
print(len(dct))       # 4

person = make_person()
print(len(person))    # 7


# -----------------------------------------------------
# 3. ACCESSING DICTIONARY ITEMS
# -----------------------------------------------------
section("3. Accessing Dictionary Items")

# Refer to the item by its KEY name
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
print(dct['key1'])    # value1
print(dct['key4'])    # value4

person = make_person()
print(person['first_name'])           # Asabeneh
print(person['country'])              # Finland
print(person['skills'])               # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person['skills'][0])            # JavaScript  (list inside a dictionary)
print(person['address']['street'])    # Space street (dictionary inside a dictionary)

# A missing key raises a KeyError
try:
    print(person['city'])
except KeyError as error:
    print("Error as expected -> KeyError:", error)

# SAFE WAY: the get() method returns None if the key does not exist
print("\nUsing get():")
print(person.get('first_name'))   # Asabeneh
print(person.get('country'))      # Finland
print(person.get('skills'))       # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person.get('city'))         # None  (NoneType)

# get() also accepts a default value to return instead of None
print(person.get('city', 'Unknown'))   # Unknown


# -----------------------------------------------------
# 4. ADDING ITEMS TO A DICTIONARY
# -----------------------------------------------------
section("4. Adding Items to a Dictionary")

# Assign a value to a NEW key
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
dct['key5'] = 'value5'
print(dct)

person = make_person()
person['job_title'] = 'Instructor'
person['skills'].append('HTML')       # modify the list stored inside
print(person)


# -----------------------------------------------------
# 5. MODIFYING ITEMS IN A DICTIONARY
# -----------------------------------------------------
section("5. Modifying Items in a Dictionary")

# Assign a new value to an EXISTING key
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
dct['key1'] = 'value-one'
print(dct)

person = make_person()
person['first_name'] = 'Eyob'
person['age'] = 252
print(person['first_name'], person['age'])   # Eyob 252


# -----------------------------------------------------
# 6. CHECKING KEYS IN A DICTIONARY
# -----------------------------------------------------
section("6. Checking Keys in a Dictionary")

# `in` checks KEYS (not values)
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
print('key2' in dct)      # True
print('key5' in dct)      # False
print('value1' in dct)    # False -> 'in' does not look at values


# -----------------------------------------------------
# 7. REMOVING KEY AND VALUE PAIRS
# -----------------------------------------------------
section("7. Removing Key and Value Pairs")

# pop(key)   -> removes the item with that key (and returns its value)
# popitem()  -> removes the LAST inserted item (and returns it)
# del d[key] -> removes the item with that key
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
dct.pop('key1')
print("After pop('key1')  :", dct)

dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
dct.popitem()
print("After popitem()    :", dct)

del dct['key2']
print("After del dct['key2']:", dct)

person = make_person()
person.pop('first_name')        # removes the first_name item
person.popitem()                # removes the LAST item -> address
del person['is_married']        # removes the is_married item
print("\nperson after removals:", person)


# -----------------------------------------------------
# 8. CHANGING DICTIONARY TO A LIST OF ITEMS
# -----------------------------------------------------
section("8. Dictionary to a List of Items - items()")

# items() gives (key, value) pairs as tuples
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
print(dct.items())
# dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])

# Wrap with list() if you want a real list of tuples
print(list(dct.items()))

# Handy in a for loop
for key, value in dct.items():
    print(key, "->", value)


# -----------------------------------------------------
# 9. CLEARING A DICTIONARY
# -----------------------------------------------------
section("9. Clearing a Dictionary - clear()")

# clear() empties the dictionary and returns None
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
print(dct.clear())    # None
print(dct)            # {}


# -----------------------------------------------------
# 10. DELETING A DICTIONARY
# -----------------------------------------------------
section("10. Deleting a Dictionary - del")

# del removes the dictionary variable completely
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
del dct

try:
    print(dct)
except NameError as error:
    print("Dictionary deleted! Error as expected ->", error)


# -----------------------------------------------------
# 11. COPYING A DICTIONARY
# -----------------------------------------------------
section("11. Copying a Dictionary - copy()")

# copy() makes a separate dictionary, so changing the copy
# does NOT change the original.
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
dct_copy = dct.copy()
dct_copy['key1'] = 'changed'
print("Original:", dct)
print("Copy    :", dct_copy)


# -----------------------------------------------------
# 12. GETTING DICTIONARY KEYS
# -----------------------------------------------------
section("12. Getting Dictionary Keys - keys()")

# keys() returns a view of all the keys (use list() for a real list)
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
keys = dct.keys()
print(keys)           # dict_keys(['key1', 'key2', 'key3', 'key4'])
print(list(keys))     # ['key1', 'key2', 'key3', 'key4']


# -----------------------------------------------------
# 13. GETTING DICTIONARY VALUES
# -----------------------------------------------------
section("13. Getting Dictionary Values - values()")

# values() returns a view of all the values (use list() for a real list)
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
values = dct.values()
print(values)         # dict_values(['value1', 'value2', 'value3', 'value4'])
print(list(values))   # ['value1', 'value2', 'value3', 'value4']


# -----------------------------------------------------
# QUICK CHEAT SHEET
# -----------------------------------------------------
"""
Operation               Code
---------------------   ----------------------------------
Empty dictionary        {} or dict()
Length                  len(d)
Access value            d['key']
Safe access             d.get('key')  /  d.get('key', default)
Add / modify item       d['key'] = value
Check a key             'key' in d
Remove by key           d.pop('key')  /  del d['key']
Remove last item        d.popitem()
List of (key, value)    d.items()
All keys                d.keys()
All values              d.values()
Empty the dictionary    d.clear()
Delete the dictionary   del d
Copy                    d.copy()
"""