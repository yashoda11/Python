# Working with Sets :

# Set Operations :

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union of two sets
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5, 6}

# Intersection of two sets
intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {3, 4}

# Difference between two sets
difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2}

# Symmetric Difference (elements in either set, but not in both)
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)  # Output: {1, 2, 5, 6}

# Membership Test :

my_set = {1, 2, 3, 4, 5}
print(3 in my_set)  # Output: True
print(6 not in my_set)  # Output: True

print("-----------------------------------------------------------------")

### Questions to practice (Day - 22):

# **Question 1: Symmetric Difference between two sets**
# Expected Input: Set A: {1, 2, 3}, Set B: {3, 4, 5}
# Expected Output: {1, 2, 4, 5}

print("Question -01")
print("Symmetric Difference between two sets :")
setA = {1, 2, 3}
setB = {3, 4, 5}
symmetric_difference_set = setA.symmetric_difference(setB)
print("The Symmetric Difference of set A", setA, "and set B", setB, "is :", symmetric_difference_set)

print("-----------------------------------------------------------------")

# **Question 2: Checking membership in a set**
# Expected Input: Set: {1, 2, 3}, Element to check: 2
# Expected Output: True

print("Question -02")
print("Checking membership in a set :")
set = {1, 2, 3}
element_to_check = 2
print("Checking whether the given element is exist or not.")
print(element_to_check in set)

print("-----------------------------------------------------------------")

# **Question 3: Union of two sets**
# Expected Input: Set A: {1, 2, 3}, Set B: {3, 4, 5}
# Expected Output: {1, 2, 3, 4, 5}

print("Question - 03  -  Union of two sets") 
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.union(set2)
print("Union of two sets", set1, "and ", set2, "is :",result)

print("-----------------------------------------------------------------")

# **Question 4: Intersection of two sets**
# Expected Input: Set A: {1, 2, 3}, Set B: {3, 4, 5}
# Expected Output: {3}

print("Question - 04  -  Intersection of two sets")
set1 = {1, 2, 3}
set2 = { 3, 4, 5}
result = set1.intersection(set2)
print("Intersection of two sets", set1, "and ", set2, "is :", result)

print("-----------------------------------------------------------------")

# **Question 5: Difference between two sets**
# Expected Input: Set A: {1, 2, 3, 4}, Set B: {3, 4, 5}
# Expected Output: {1, 2}

print("Question - 05  -  Difference between two sets ")
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}
result = set1.difference(set2)
print("Difference between two sets", set1, "and", set2, "is :", result)

print("-----------------------------------------------------------------")

# **Question 6: Removing duplicate elements from a list using a set**
# Expected Input: List: [1, 2, 2, 3, 4, 4, 5]
# Expected Output: [1, 2, 3, 4, 5]

# print("Question - 06  -  Removing duplicate elements from a list using a set ")
# given_list = [1, 2, 2, 3, 4, 4, 5]
# updated_
# for elme

print("-----------------------------------------------------------------")
print("Question -07")

print("-----------------------------------------------------------------")
print("Question -08")
print("-----------------------------------------------------------------")


print("Question -09")

print("-----------------------------------------------------------------")

print("Question -10")

print("-----------------------------------------------------------------")

