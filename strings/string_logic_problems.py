# string_logic_problems.py
# Python String Logic Practice


# 1. Reverse a string
text = "Python"
reversed_text = text[::-1]
print("Reversed:", reversed_text)


# 2. Count vowels in a string
sentence = "Artificial Intelligence"
vowels = "aeiouAEIOU"
count = 0

for char in sentence:
    if char in vowels:
        count += 1

print("Vowel count:", count)


# 3. Check if a word is palindrome
word = "level"

if word == word[::-1]:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")


# 4. Count characters in a string
sample = "Data Science"

characters = 0
for char in sample:
    if char != " ":
        characters += 1

print("Total characters (without spaces):", characters)


# 5. Find the longest word in a sentence
sentence = "Python makes data analysis powerful"

words = sentence.split()
longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print("Longest word:", longest_word)
