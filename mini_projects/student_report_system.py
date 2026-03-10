# student_report_system.py
# Python Mini Project – Student Report System


# Dictionary storing student marks
students = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 90,
    "David": 65,
    "Eva": 78
}

# Display all student marks
print("Student Marks:")
for name, marks in students.items():
    print(name, ":", marks)


# Find top student
top_student = ""
highest_marks = 0

for name, marks in students.items():
    if marks > highest_marks:
        highest_marks = marks
        top_student = name

print("\nTop Student:", top_student)
print("Highest Marks:", highest_marks)


# Calculate average marks
total = 0
for marks in students.values():
    total += marks

average = total / len(students)

print("\nAverage Marks:", average)
