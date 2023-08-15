# Example: Equality and inequality comparison
string1 = "hello"
string2 = "Hello"

if string1 == string2:
    print("Both strings are equal.")
else:
    print("The strings are not equal.")

if string1 != string2:
    print("The strings are not equal.")
else:
    print("Both strings are equal.")

print("---------------------------------------")

# Example: Lexicographical comparison
string1 = "apple"
string2 = "banana"

if string1 < string2:
    print("string1 comes before string2.")
else:
    print("string1 comes after or is equal to string2.")

if string1 <= string2:
    print("string1 comes before or is equal to string2.")
else:
    print("string1 comes after string2.")

if string1 > string2:
    print("string1 comes after string2.")
else:
    print("string1 comes before or is equal to string2.")

if string1 >= string2:
    print("string1 comes after or is equal to string2.")
else:
    print("string1 comes before string2.")

print("---------------------------------------")

### Questions to practice (Day - 16):

# 1. Given two strings "Python" and "python", check if they are equal using the equality operator (`==`).
# Input: "Python", "python"
# Expected Output: False

print("Question = 01")
string1 = "Python"
string2 = "python"

if string1 == string2:
    print(True)
else :
    print(False)


print("---------------------------------------")

# 2. Write a Python function that takes a string as input and checks if it is an empty string using the equality operator (`==`).
# Input: ""
# Expected Output: True

print("Question - 02")
string = input("Enter a String : ")
if string == "":
    print(True)
else:
    print(False)