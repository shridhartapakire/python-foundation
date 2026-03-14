# file_read_write.py
# Python File Handling Practice


# Writing to a file
with open("sample.txt", "w") as file:
    file.write("Hello, this is my first file handling program.\n")
    file.write("Learning Python step by step.")


# Reading from a file
with open("sample.txt", "r") as file:
    content = file.read()
    print("File Content:")
    print(content)


# Appending data to the file
with open("sample.txt", "a") as file:
    file.write("\nThis line was added later.")


# Reading again after appending
with open("sample.txt", "r") as file:
    print("\nUpdated File Content:")
    print(file.read())
