# function_with_input.py
# Python Foundation – Functions with User Input


# Function to calculate square of a number
def square(num):
    return num * num


# Function to find the largest of two numbers
def find_largest(a, b):
    if a > b:
        return a
    else:
        return b


# Function to count vowels in a word
def count_vowels(word):
    vowels = "aeiouAEIOU"
    count = 0

    for char in word:
        if char in vowels:
            count += 1

    return count


# Main program
number = int(input("Enter a number: "))
print("Square:", square(number))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Largest number:", find_largest(a, b))

text = input("Enter a word: ")
print("Number of vowels:", count_vowels(text))
