# String Indexing :

# Define a string
my_string = "Hello, world!"

# Access the first character of the string
first_character = my_string[0]

# Print the result
print(first_character) 

# Define a string
my_string = "Hello, world!"

# Access the last character of the string
last_character = my_string[-1]

# Print the result
print(last_character)

s = "NIHAR"

# Accessing individual characters using negative indexing
last_char = s[-1]  # 'R'
second_last_char = s[-2]  # 'A'
third_last_char = s[-3]  # 'H'
fourth_last_char = s[-4]  # 'I'
first_char = s[-5]  # 'N'

print("Last character:", last_char)
print("Second last character:", second_last_char)
print("Third last character:", third_last_char)
print("Fourth last character:", fourth_last_char)
print("First character:", first_char)

# String Slicing :
# Define a string
my_string = "Hello, world!"

# Extract the first five characters of the string
substring = my_string[0:5]

# Print the result
print(substring)

# Define a string
my_string = "Hello, world!"

# Extract a range of characters from the string
substring = my_string[1:8]

# Print the result
print(substring)

### Questions to practice (Day 6):

# 1. Example: Get the first character of the sentence.
# Input: "The sun is shining."
# Output: "T"

sentence = "The sun is shining."
print("The First Character of the Sentence(", sentence ,") is :", sentence[0])

# 2. Example: Get the last character of the sentence.
# Input: "She sells seashells by the seashore."
# Output: "."

sentence = "She sells seashells by the seashore."
print("The Last Character of the Sentence(", sentence ,") is :", sentence[-1])

# 3. Example: Get the character at index 3.
# Input: "I love Python!"
# Output: "o"

sentence = "I love Python!"
print("The Character at the index of 3 in the Sentence(", sentence ,") is :", sentence[3])

# 4. Example: Get the second last character of the sentence.
# Input: "Life is beautiful."
# Output: "l"

sentence = "Life is beautiful."
print("The Second Last Character of the Sentence(", sentence ,") is :", sentence[-2])

# 5. Example: Get a substring from index 7 to index 14 (exclusive).
# Input: "Welcome to Python programming."
# Output: " to Pyt"

sentence = "Welcome to Python programming."
print("A substring from index 7 to index 14 (exclusive) is :" , sentence[7:14])

# 6. Example: Get a substring from index -9 to -3.
# Input: "The future is bright."
# Output: "s brig"

sentence = "The future is bright."
print("A substring from index -9 to index -3 (exclusive) is :" , sentence[-9:-3])

# 7. Example: Get the first six characters of the sentence.
# Input: "Good things take time."
# Output: "Good t"

sentence = "Good things take time."
print("The First Six Characters of the given sentence is :", sentence[0:6])

# 8. Example: Reverse the sentence using slicing.
# Input: "Python is awesome!"
# Output: "!emosewa si nohtyP"

sentence = "Python is awesome!"
print("The Given Sentence is :", sentence)
print("The Reverse of the given sentence using slicing is :", sentence[::-1] )

# 9. Example: Get the length of the sentence using indexing.
# Input: "Coding is fun!"
# Output: 14

sentence = "Coding is fun!"
print("1. The length of the given Sentence(" , sentence, ") :", len(sentence))

print("2.", len(sentence[:]))

length = 0
for char in sentence:
    length += 1
print("3.", length)