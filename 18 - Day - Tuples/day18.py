# Example: Creating a tuple
fruits = ("apple", "banana", "orange")
coordinates = (3.14, 2.71)

# Example: Accessing elements in a tuple
fruits = ("apple", "banana", "orange")

print(fruits[0])  # Output: "apple"
print(fruits[2])  # Output: "orange"

# Example: Tuple packing and unpacking
person = ("John", 30, "New York")
name, age, city = person

print(name)  # Output: "John"
print(age)   # Output: 30
print(city)  # Output: "New York"

# Example: Tuple functions
numbers = (5, 2, 8, 1, 7)

# Length of the tuple
length = len(numbers)
print(length)  # Output: 5

# Maximum and minimum elements in the tuple
maximum = max(numbers)
minimum = min(numbers)
print(maximum, minimum)  # Output: 8 1

# Example: Tuple concatenation and repetition
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenation
result = tuple1 + tuple2
print(result)  # Output: (1, 2, 3, 4, 5, 6)

# Repetition
repeated_tuple = tuple1 * 3
print(repeated_tuple)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)

print("---------------------------------------------------------")

# Questions to practice (Day - 18):

# 1.  Create a tuple containing three elements: 'apple', 5, and True.
# Expected Input: No input required.
# Expected Output: ('apple', 5, True)

print("Question - 01")
elements = ('apple', 5, True)
print(elements)

print("---------------------------------------------------------")

# 2.  Access the second element from the given tuple: ('cat', 'dog', 'bird', 'fish').
# Expected Input: No input required.
# Expected Output: 'dog'

print("Question - 02")
elements = ('cat', 'dog', 'bird', 'fish')
element = elements[1]
print(element)

print("---------------------------------------------------------")

# 3.  Concatenate two tuples: (1, 2, 3) and ('a', 'b', 'c').
# Expected Input: No input required.
# Expected Output: (1, 2, 3, 'a', 'b', 'c')

print("Question - 03")
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
tuple = tuple1 + tuple2
print(tuple)

print("---------------------------------------------------------")

# 4.  Find the length of the tuple: (10, 20, 30, 40, 50).
# Expected Input: No input required.
# Expected Output: 5

print("Question - 04")
tuple = (10, 20, 30, 40, 50)
length = len(tuple)
print("The Length of the given Tuple", tuple, "is :", length)

print("---------------------------------------------------------")

# 5.  Check if the element 25 exists in the tuple: (10, 20, 30, 40, 50).
# Expected Input: No input required.
# Expected Output: False

print("Question - 05")
tuple = (10, 20, 30, 40, 50)
element = 25

if element in tuple :
    print(True)
else:
    print(False)

print("---------------------------------------------------------")

# 6.  Create a new tuple with elements from the given tuple (3, 6, 9) repeated 3 times.
#  Expected Input: No input required.
#  Expected Output: (3, 6, 9, 3, 6, 9, 3, 6, 9)

print("Question - 06")
tuple = (3, 6, 9)
new_tuple = tuple * 3
print(new_tuple)

print("---------------------------------------------------------")

# 7.   Perform packing and unpacking on a tuple containing the names of three fruits: 'apple', 'banana', and 'orange'. Use unpacking to assign each fruit to three variables: fruit1, fruit2, and fruit3.
# Expected Input: No input required.
# Expected Output:
# fruit1 = 'apple'
# fruit2 = 'banana'
# fruit3 = 'orange'

print("Question - 07")
fruits = ('apple', 'banana', 'orange')
fruits1, fruits2, fruits3 = fruits
print("fruits1 :", fruits1)
print("fruits2 :", fruits2)
print("fruits3 :", fruits3)