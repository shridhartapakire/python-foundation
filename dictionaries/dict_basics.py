# dict_basics.py
# Python Foundation – Dictionary Basics


# Creating a dictionary
student = {
    "name": "Shridhar",
    "age": 20,
    "course": "AI & DS"
}

# Accessing dictionary values
print("Student Name:", student["name"])
print("Course:", student["course"])


# Adding a new key-value pair
student["grade"] = "A"
print("Updated dictionary:", student)


# Modifying a value
student["age"] = 21
print("After modifying age:", student)


# Looping through dictionary keys and values
print("Student details:")
for key, value in student.items():
    print(key, ":", value)
