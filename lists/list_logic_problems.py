# list_logic_problems.py
# Python Foundation – List Logic Problems


# Find the maximum number in a list
numbers = [12, 45, 7, 23, 56, 89, 34]

max_number = numbers[0]

for num in numbers:
    if num > max_number:
        max_number = num

print("Maximum number:", max_number)


# Count positive and negative numbers
values = [10, -5, 7, -2, 3, -8, 15]

positive_count = 0
negative_count = 0

for val in values:
    if val > 0:
        positive_count += 1
    elif val < 0:
        negative_count += 1

print("Positive numbers:", positive_count)
print("Negative numbers:", negative_count)


# Calculate sum of list elements
nums = [5, 10, 15, 20]

total = 0
for n in nums:
    total += n

print("Sum of list:", total)
