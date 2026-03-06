# list_basics.py
# Python Foundation – List Basics


# Creating a list
numbers = [10, 20, 30, 40, 50]

# Accessing elements
print("First element:", numbers[0])
print("Last element:", numbers[-1])


# Modifying an element
numbers[2] = 35
print("Modified list:", numbers)


# Adding elements
numbers.append(60)
print("After append:", numbers)


# Removing elements
numbers.remove(20)
print("After removing 20:", numbers)


# Looping through a list
print("Printing list elements:")
for num in numbers:
    print(num)
