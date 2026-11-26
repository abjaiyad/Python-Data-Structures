person = {
    "first_name": "Amad",
    "last_name": "Jaiyad",
    "age": 201,
    "country": "India",
    "is_married": False,
    "skills": ["Python", "SQL", "DSA", "Git"],
    "address": {
        "street": "Space Street",
        "city": "Gurgaon",
        "state": "Haryana",
        "zip_code": "122016"
    }
}


# Check if the key 'skills' exists in the dictionary
if 'skills' in person:
    print("Skills key exists in the dictionary.")

# Check if the key 'address' exists in the dictionary
if 'address' in person:
    print("Address key exists in the dictionary.")

# Check if the key 'phone_number' exists in the dictionary
if "phone_number" in person:
    print("Phone Number key exists in the dictionary.")

# Get the value of the 'skills' key
skills = person.get("skills")
print("Skills:", skills)

# Get the value of the 'address' key
address = person.get("address")
print("Address:", address)

# Get the value of the 'phone' key
phone = person.get("phone")
print("Phone:", phone)

# Get the value of the 'first_name' key
first_name = person.get("first_name")
print("First Name:", first_name)

# Get the value of the 'last_name' key
last_name = person.get("last_name")
print("Last Name:", last_name)

# Get the value of the 'age' key
age = person.get("age")
print("Age:", age)

# Get the value of the 'country' key
country = person.get("country")
print("Country:", country)

# Get the value of the 'is_married' key
is_married = person.get("is_married")
print("Is Married:", is_married)

# Get the value of the 'street' key from the 'address' dictionary
street = person.get("address", {}).get("street")
print("Street:", street)

# Get the value of the 'city' key from the 'address' dictionary
city = person.get("address", {}).get("city")
print("City:", city)

# Get the value of the 'state' key from the 'address' dictionary
state = person.get("address", {}).get("state")
print("State:", state)

# Get the value of the 'zip_code' key from the 'address' dictionary
zip_code = person.get("address", {}).get("zip_code")
print("Zip Code:", zip_code)

# Get the value of the 'skills' key and check if it contains 'Python'
if skills and "Python" in skills:
    print("Python is in the skills list.")

# Get the value of the 'skills' key and check if it contains 'Java'
if skills and "Java" not in skills:
    print("Java is not in the skills list.")

# Get the value of the 'skills' key and check if it contains 'SQL'
if skills and "SQL" in skills:
    print("SQL is in the skills list.")

# Get the value of the 'skills' key and check if it contains 'DSA'
if skills and "DSA" in skills:
    print("DSA is in the skills list.")

# Get the value of the 'skills' key and check if it contains 'Git'
if skills and "Git" in skills:
    print("Git is in the skills list.")

# Get the value of the 'skills' key and check if it contains 'C++'
if skills and "C++" not in skills:
    print("C++ is not in the skills list.")

# Get the value of the 'skills' key and check if it contains 'JavaScript'
if skills and "JavaScript" not in skills:
    print("JavaScript is not in the skills list.")

# Get the value of the 'skills' key and check if it contains 'HTML'
if skills and "HTML" not in skills:
    print("HTML is not in the skills list.")

# Get the value of the 'skills' key and check if it contains 'CSS'
if skills and "CSS" not in skills:
    print("CSS is not in the skills list.")

# Get the value of the 'skills' key and check if it contains 'React'
if skills and "React" not in skills:
    print("React is not in the skills list.")

# Get the value of the 'skills' key and check if it contains 'Node.js'
if skills and "Node.js" not in skills:  
    print("Node.js is not in the skills list.")

# Get the value of the 'skills' key and check if it contains 'Django'
if skills and "Django" not in skills:   
    print("Django is not in the skills list.")

# If the key 'skills' exists in the dictionary, print the skills
if 'skills' in person:
    print("Skills:", person['skills'])

# If the key 'address' exists in the dictionary, print the address
if "address" in person:
    print("Address:", person['address'])
    
# Want to practice more? You can try adding more keys to the dictionary, 
# such as 'email', 'phone_number', 
# or 'hobbies', and then check if those keys exist and retrieve their values. 
# You can also practice updating existing keys or adding new skills to the 'skills' list.

person['email'] = 'amad.jaiyad@example.com'
person['phone_number'] = '+91-1234567890'
person['hobbies'] = ['Reading', 'Traveling', 'Gaming']

# Check if the key 'email' exists in the dictionary
if "email" in person:
    print("Email:", person['email'])

# Check if the key 'phone_number' exists in the dictionary
if "phone_number" in person:
    print("Phone Number:", person['phone_number'])

# Check if the key 'hobbies' exists in the dictionary
if "hobbies" in person:
    print("Hobbies:", person['hobbies'])

# Add a new skill to the 'skills' list
person['skills'].append('JavaScript')
print("Updated Skills:", person['skills'])

# Update the 'age' key in the dictionary
person['age'] = 202
print("Updated Age:", person['age'])

# Update the 'is_married' key in the dictionary
person['is_married'] = True
print("Updated Is Married:", person['is_married'])

# Update the 'address' key in the dictionary
person['address']['street'] = 'Galaxy Street'
print("Updated Address:", person['address'])

# You can also practice removing keys from the dictionary using the `del` statement or the `pop()` method.
# For example, you can remove the 'hobbies' key from the dictionary.

# Remove the 'hobbies' key from the dictionary
del person['hobbies']

# Check if the key 'hobbies' exists in the dictionary after removal
if "hobbies" not in person:
    print("Hobbies key has been removed from the dictionary.")

# You can also practice iterating over the dictionary to print all keys and values.

# Iterate over the dictionary and print all keys and values
for key, value in person.items():
    print(f"{key}: {value}")

# You can also practice using dictionary comprehensions to create new dictionaries based on existing ones.
# For example, you can create a new dictionary that contains only the keys and values where the value is not None.
filtered_person = {key: value for key, value in person.items() if value is not None}
print("Filtered Dictionary:", filtered_person)

# You can also practice using the `update()` method to update multiple keys in the dictionary at once.
# For example, you can update the 'first_name' and 'last_name' keys in the dictionary.
person.update({"first_name": "Bloody", "last_name": "Developer"})
print("Updated First Name:", person['first_name'])
print("Updated Last Name:", person['last_name'])

# You can also practice using the `clear()` method to remove all keys and values from the dictionary.
# For example, you can clear the entire dictionary.

# Clear the entire dictionary
person.clear()
print("Cleared Dictionary:", person)