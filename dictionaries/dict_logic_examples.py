# dict_logic_examples.py
# Python Foundation – Dictionary Logic Examples


# Dictionary of student marks
marks = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 90,
    "David": 65,
    "Eva": 78
}

# Find student with highest marks
highest_student = ""
highest_marks = 0

for student, score in marks.items():
    if score > highest_marks:
        highest_marks = score
        highest_student = student

print("Top student:", highest_student)
print("Highest marks:", highest_marks)


# Count students who scored above 75
count = 0

for score in marks.values():
    if score > 75:
        count += 1

print("Students scoring above 75:", count)


# Print all students and their marks
print("Student Marks:")
for student, score in marks.items():
    print(student, ":", score)
