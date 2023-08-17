# Creating a Set:
# Using curly braces
my_set = {1, 2, 3, 4, 5}

print(my_set)

# Using the set() constructor
another_set = set([5, 6, 7, 8, 9])

print(another_set)

# Adding Elements to a Set:
my_set = {1, 2, 3}
my_set.add(4)
my_set.add(5)
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Removing Elements from a Set:
my_set = {1, 2, 3, 4, 5}
my_set.remove(3)
print(my_set)  # Output: {1, 2, 4, 5}

# Remove an element without raising an error if the element is not present
my_set.discard(10)

# Pop removes and returns an arbitrary element from the set
popped_element = my_set.pop()
print(popped_element, my_set)  # Output (random order): 1, {2, 4, 5}

print("-----------------------------------------------------------------")

# Questions to practice (Day - 21):

# **Question 1: Creating a set**
# Expected Input: None
# Expected Output: An empty set

print("Question - 01")
my_set = set()
print(my_set)

print("-----------------------------------------------------------------")

# **Question 2: Adding elements to a set**
# Expected Input: Set: {1, 2, 3}, Element to add: 4
# Expected Output: Set: {1, 2, 3, 4}

print("Question - 02")
my_set = {1, 2, 3}
print(my_set)
my_set.add(4)
print("Adding elements to a set : ")
print(my_set)

print("-----------------------------------------------------------------")

# **Question 3: Removing an element from a set**
# Expected Input: Set: {1, 2, 3, 4}, Element to remove: 3
# Expected Output: Set: {1, 2, 4}

print("Question - 03")
my_set = {1, 2, 3, 4}
print(my_set)
my_set.remove(3)
print("Removing an element from a set")
print(my_set)

print("-----------------------------------------------------------------")

# **Question 4: Removing a non-existent element from a set**
# Expected Input: Set: {1, 2, 3, 4}, Element to remove: 5
# Expected Output: Set: {1, 2, 3, 4}

print("Question - 04")
my_set = {1, 2, 3, 4}
print(my_set)
my_set.discard(5)
print(my_set)

print("-----------------------------------------------------------------")

# **Question 5: Creating a set from a list**
# Expected Input: List: [5, 10, 15, 20]
# Expected Output: Set: {5, 10, 15, 20}

print("Question - 05")
list = set([5, 10, 15, 20])
print(list)

print("-----------------------------------------------------------------")

# **Question 6: Adding multiple elements to a set**
# Expected Input: Set: {1, 2, 3}, Elements to add: {4, 5}
# Expected Output: Set: {1, 2, 3, 4, 5}

print("Question - 06")
my_set = {1, 2, 3}
print(my_set)
my_set.add(4)
my_set.add(5)
print("Adding multiple elements to a set")
print(my_set)

print("-----------------------------------------------------------------")

# **Question 7: Removing elements using discard()**
# Expected Input: Set: {10, 20, 30, 40}, Elements to remove: {20, 50}
# Expected Output: Set: {10, 30, 40}

print("Question - 07")
my_set = {10, 20, 30, 40}
print(my_set)
my_set.discard(20)
my_set.discard(50)
print("Removing elements using 'discard()'")
print(my_set)

print("-----------------------------------------------------------------")