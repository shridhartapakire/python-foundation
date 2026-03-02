# loop_logic_problems.py
# Python Foundation – Loop Logic Problems

# Problem 1: Sum of first n natural numbers
n = 10
total = 0
for i in range(1, n + 1):
    total += i
print("Sum of first", n, "numbers:", total)

# Problem 2: Count even and odd numbers in a list
numbers = [1, 4, 7, 9, 12, 16, 19]
even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even count:", even_count)
print("Odd count:", odd_count)

# Problem 3: Check if a number is prime
num = 17
is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
