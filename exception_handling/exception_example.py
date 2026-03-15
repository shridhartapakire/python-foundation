# exception_example.py
# Python Exception Handling


# Handling a division by zero error
try:
    x = 5 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")


# Handling a file not found error
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"Error: {e}")


# Using else to handle no errors
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Can't divide by zero.")
else:
    print(f"Result: {x}")


# Using finally to close a file or cleanup
try:
    file = open("sample.txt", "w")
    file.write("This is an example.")
except Exception as e:
    print(f"Error: {e}")
finally:
    file.close()
    print("File is closed.")
