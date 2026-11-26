# Create an empty dictionary called dog
dog = {}

# Add name, color, breed, legs, age to the dog dictionary
dog["name"] = "Buddy"
dog["color"] = "Black"
dog["breed"] = "Labrador"
dog["legs"] = 4
dog["age"] = 3

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    "first_name": "Sahil",
    "last_name": "Jaiyad",
    "gender": "Male",
    "age": 22,
    "is_married": False,
    "skills": ["Python", "SQL", "DSA", "Git"],
    "address": {
        "country": "India",
        "city": "Cyber City"
    }
}

# Get the length of the student dictionary
print("Length of student dictionary:", len(student))

# Get the value of skills and check the data type, it should be a list
print("Skills:", student["skills"])
print("Type of skills:", type(student["skills"]))

# Modify the skills values by adding one or two skills
student["skills"].append("Machine Learning")
student["skills"].append("Data Analysis")

# Get the dictionary keys as a list
print("Keys of student dictionary:", list(student.keys()))

# Get the dictionary values as a list
print("Values of student dictionary:", list(student.values()))

# Change the dictionary to a list of tuples using items() method
print("Items of student dictionary:", list(student.items()))

# Delete one of the items in the dictionary
del student["is_married"]

# Delete one of the dictionaries
del student