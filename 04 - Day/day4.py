### Questions to Solve (Day - 4):

a = "Nihar " * 5
print(a)

s = "Arrow"
s = ("* " * 3) + s + (" *" * 3)
print(s)

# 1. Concatenate two strings `str1` and `str2`, and print the result.
#     - **Expected Input:** str1 = "Hello", str2 = "World"
#     - **Expected Output:** "HelloWorld"

str1 = "Hello"
str2 = "World"
print(str1 + str2)

# 2. Ask the user to enter their name and a greeting. Concatenate the name and greeting to form a personalized message and print it.
#     - **Expected Input:** name = "John", greeting = "Hi"
#     - **Expected Output:** "Hi John"

name = input("Enter Your Name : ")
greeting = input("Enter Your greeting : ")
print(greeting + " " + name)

# 3. Create a string `word` and repeat it 5 times. Print the result.
#     - **Expected Input:** word = "Python"
#     - **Expected Output:** "PythonPythonPythonPythonPython"

word = "Python"
print(word * 5)

# 4. Ask the user to enter a word and a number. Repeat the word as many times as the given number and print the result.
#     - **Expected Input:** word = "Hello", number = 3
#     - **Expected Output:** "HelloHelloHello"

word = "Hello"
number = 3
print(word * number)

word = input("Enter a Word : ")
number = int(input("Enter a Number : "))
print(word * number)

# 5. Create a string `sentence` and find its length. Print the length of the sentence.
#     - **Expected Input:** sentence = "This is a sample sentence."
#     - **Expected Output:** 27

sentence1 = "This is a sample sentence. "
Length1 = len(sentence1)
print("The length of the sentence is :", Length1)

# 6. Ask the user to input a sentence. Find the length of the sentence, and print the last character of the sentence.
#     - **Expected Output:** Length of the sentence and the last character.

sentance = input("Enter a Sentance : ")
Length = len(sentance)
print("The Length of the Sentance is : ", Length, "\nThe Last character of the sentance(",sentance,") is :", sentance[-1])

# 7. Create two strings `str1` and `str2`. Find the lengths of both strings and concatenate them. Print the concatenated string.
#     - **Expected Input:** str1 = "Hello", str2 = "World"
#     - **Expected Output:** "HelloWorld"

str1 = "Hello"
str2 = "World!"
str1_length = len(str1)
str2_length = len(str2)
print(str1 + str2)
print( str1_length , str2_length)

# 8. Ask the user to enter two words, `word1` and `word2`. Concatenate the two words with a space in between and print the result.
#     - **Expected Input:** word1 = "Hello", word2 = "Python"
#     - **Expected Output:** "Hello Python"

word1 = input("Enter a Word1 : ")
word2 = input("Enter a Word2 : ")
print(word1, " ", word2)

# 9. Create a string `pattern` containing "*" character and repeat it to form a pattern. The pattern should have 5 rows. Print the resulting pattern.
#     - **Expected Output:**
# *
# **
# ***
# ****
# *****

pattern = "*"
print(pattern)
print(pattern * 2)
print(pattern * 3)
print(pattern * 4)
print(pattern * 5)