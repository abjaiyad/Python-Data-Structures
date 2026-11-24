# Create an empty tuple
empty_tuple = ()

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ('Alice', 'Bob', 'Charlie')  # Replace with actual names
brothers = ('David', 'Eve', 'Frank')   # Replace with actual names

# Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers

# How many siblings do you have?
num_siblings = len(siblings)

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + ('John', 'Jane')  # Replace with actual names

print("Number of siblings:", num_siblings)
print("Family members:", family_members)

# Unpack siblings and parents from family_members
siblings_unpacked = family_members[:-2]
parents_unpacked = family_members[-2:]

print("Siblings unpacked:", siblings_unpacked)
print("Parents unpacked:", parents_unpacked)

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("banana", "orange", "mango", "lemon")
vegetables = ("Tomato", "Potato", "Cabbage", "Onion", "Carrot")
animal_products = ("milk", "meat", "eggs", "cheese")

food_stuff_tp = fruits + vegetables + animal_products

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_items = food_stuff_lt[len(food_stuff_lt)//2-1:len(food_stuff_lt)//2+1]

# Slice out the first three items and the last three items from food_stuff_lt list
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]

# Delete the food_stuff_tp tuple completely
del food_stuff_tp

# Check if an item exists in tuple:
print("banana" in food_stuff_lt)  # True
print("potato" in food_stuff_lt)  # True

# Check if 'Estonia' is a nordic country
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)  # False

# Check if 'Iceland' is a nordic country
print("Iceland" in nordic_countries)  # True
