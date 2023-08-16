# Example: Creating a list of numbers
numbers = [1, 2, 3, 4, 5]

# Creating a list of strings
fruits = ["apple", "banana", "orange"]

# Creating a mixed-type list
mixed_list = [1, "apple", True, 3.14]

# Example: Accessing elements in a list
fruits = ["apple", "banana", "orange"]

print(fruits)
print(fruits[0])  # Output: "apple"
print(fruits[2])  # Output: "orange"

# Example: Modifying elements in a list
fruits = ["apple", "banana", "orange"]
fruits[1] = "grape"
print(fruits)  # Output: ['apple', 'grape', 'orange']

# Example: List operations
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenation
result = list1 + list2
print(result)  # Output: [1, 2, 3, 4, 5, 6]

# Repetition
repeated_list = list1 * 3
print(repeated_list)  # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Example: List methods
fruits = ["apple", "banana", "orange"]

# Adding elements
fruits.append("grape")
print(fruits)  # Output: ['apple', 'banana', 'orange', 'grape']

# Removing elements
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'orange', 'grape']

# Sorting elements
fruits.sort()
print(fruits)  # Output: ['apple', 'grape', 'orange']

print("----------------------------")

# 1. Write a Python program that takes a list of numbers [1, 2, 3, 4, 5] and prints each number on a new line.
# Input: [1, 2, 3, 4, 5]
# Expected Output:
# 1
# 2
# 3
# 4
# 5

print("Question - 01")
my_list = [1, 2, 3, 4, 5]
for num in my_list:
    print(num)

print("----------------------------")

# 2. Given a list of strings ["apple", "banana", "orange"], concatenate all the strings together with a space in between and print the result.
# Input: ["apple", "banana", "orange"]
# Expected Output: "apple banana orange"

print("Question - 02")
list_of_strings = ["apple", "banana", "orange"]
result = " ".join(list_of_strings)
print(result)

print("----------------------------")

# 3. Write a Python function that takes a list of numbers as input and returns the sum of all the numbers.
# Input: [1, 2, 3, 4, 5]
# Expected Output: 15

print("Question - 03")

input_numbers = input("Enter a list of Numbers (Space Seperated) : ")
list_numbers = [int(num) for num in input_numbers.split()]
sum_of_numbers = sum(list_numbers)
print("The Sum of Numbers for the given List numbers", list_numbers, "is :", sum_of_numbers)

print("----------------------------")

# 4. Given a list of numbers [10, 20, 30, 40, 50], find the maximum number using the `max()` function and print the result.
# Input: [10, 20, 30, 40, 50]
# Expected Output: 50

print("Question - 04")
list_of_numbers = [10, 20, 30, 40, 50]
maximum_number = max(list_of_numbers)
print("The Maximum Number in the given numbers", list_of_numbers, "is :", maximum_number)

print("----------------------------")

# 5. Write a Python program that takes a list of names ["Alice", "Bob", "Charlie"] and checks if a given name (e.g., "Alice") is present in the list. Print "Name found" if the name is in the list; otherwise, print "Name not found".
# Input: Names = ["Alice", "Bob", "Charlie"], Name = "Alice"
# Expected Output: "Name found"

print("Question - 05")
list_of_names = ["Alice", "Bob", "Charlie"]
given_name = "Alice"
if given_name in list_of_names :
    print("Name Found")
else :
    print("Name not found")

print("-Input Method-")
input_names = input("Enter Names (Space-seperated) : ")
names = [name for name in input_names.split()]
gi_name = input("Enter a name to check : ")

if gi_name in names:
    print ("Name found")
else :
    print("Name not found")