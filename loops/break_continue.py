# break_continue.py
# Python Foundation – break and continue

# Example 1: Stop the loop when number is 5
for i in range(1, 11):
    if i == 5:
        break
    print(i)

# Example 2: Skip numbers divisible by 3
for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i)

# Example 3: Find a number in a list
numbers = [2, 4, 6, 8, 10, 12]
target = 8

for num in numbers:
    if num == target:
        print("Number found:", num)
        break
