# oop_basics.py
# Python Object-Oriented Programming Basics


# Creating a class
class Student:

    # constructor
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    # method to display student info
    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)


# Creating objects
student1 = Student("Alice", 20, "AI")
student2 = Student("Bob", 22, "Data Science")

# Calling methods
student1.display_info()
print()
student2.display_info()
