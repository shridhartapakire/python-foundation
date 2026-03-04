# basic_functions.py
# Python Foundation – Basic Function Examples


# Function to add two numbers
def add_numbers(a, b):
    return a + b


# Function to check if a number is even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


# Function to calculate factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Using the functions
print("Sum:", add_numbers(5, 3))
print("Number is:", check_even_odd(10))
print("Factorial:", factorial(5))
