print("AND Operator :")
# Example 1: Using 'and' with boolean variables
a = True
b = False

result = a and b
print(result)  # Output: False

# Example 2: Using 'and' with expressions
x = 10
y = 5

result = (x > 0) and (y < 10)
print(result)  # Output: True

result = (x > 0) and (y > 10)
print(result)  # Output: False

print("Or Operator :")

# Example 1: Using 'or' with boolean variables
a = True
b = False

result = a or b
print(result)  # Output: True

# Example 2: Using 'or' with expressions
x = 10
y = 5

result = (x > 0) or (y < 10)
print(result)  # Output: True

result = (x < 0) or (y > 10)
print(result)  # Output: False

print("NOT Operator :")

# Example 1: Using 'not' with boolean variable
a = True

result = not a
print(result)  # Output: False

# Example 2: Using 'not' with an expression
x = 10
y = 5

result = not (x > y)
print(result)  # Output: False

result = not (x < y)
print(result)  # Output: True

print("complex logical operations ")
# Complex example using all logical operators
x = 5
y = 10
z = 15

result = (x < y) and (y < z) or (x == z)
print(result)  # Output: True

### Questions to practice (Day 8):

# 1. Example: "and" operator with two True conditions
# Input: (10 > 5) and ("apple" == "apple")
# Output: True

print("Question - 01")
x = (10 > 5)
y = ("apple" == "apple")
result = x and y
print(result)

# 2. Example: "and" operator with one False condition
# Input: (3 < 2) and ("banana" == "orange")
# Output: False

print("Question - 02")
x = (3 < 2)
y = ("banana" == "orange")
result = x and y
print(result)

# 3. Example: "and" operator with one True and one False condition
# Input: (5 >= 3) and (10 != 10)
# Output: False

print("Question - 03")
x = (5 >= 3)
y = (10 != 10)
result = x and y
print(result)

# 4. Example: "or" operator with two True conditions
# Input: ("car" == "car") or (7 < 9)
# Output: True

print("Question - 04")
x = ("car" == "car")
y = (7 < 9)
result = x or y
print(result)

# 5. Example: "or" operator with one False condition
# Input: ("dog" == "cat") or (6 < 10)
# Output: True


print("Question - 05")
x = ("dog" == "cat")
y = (6 < 10)
result = x or y
print(result)

# 6. Example: "or" operator with both False conditions
# Input: (2 == 3) or (8 > 15)
# Output: False

print("Question - 06")
x = (2 == 3)
y = (8 > 15)
result = x or y
print(result)

# 7. Example: "not" operator with True condition
# Input: not (4 <= 3)
# Output: True

print("Question - 07")
x = (4 <= 3)
result = not x 
print(result)

# 8. Example: "not" operator with False condition
# Input: not ("orange" == "orange")
# Output: False

print("Question - 08")
x =  ("orange" == "orange")
result = not x 
print(result)

# 9. Example: "not" operator with "and" and "or"
# Input: not ((5 > 3) and ("apple" != "banana"))
# Output: False

print("Question - 09")
x = (5 > 3)
y = ("apple" != "banana")
result = not(x and y)
print(result)

# 10. Example: "and" and "not" operators combined
# Input: (10 > 5) and not (3 < 2)
# Output: True

print("Question - 10")
x = (10 > 5)
y = not(3 < 2)
result = x and y
print(result)

# 11. Example: "or" and "not" operators combined
# Input: ("cat" == "cat") or not (6 > 10)
# Output: True

print("Question - 11")
x = ("cat" == "cat")
y = not (6 > 10)
result = x or y
print(result)

# 12. Example: Using parentheses for grouping expressions
# Input: ((5 >= 3) and (10 != 10)) or (8 > 15)
# Output: False

print("Question - 12")
x = (5 >= 3)
y = (10 != 10)
reult1 = a and y
z = (8 > 15)
result = reult1 and z
print(result)

# 13. Example: Combining multiple "and" operators
# Input: (2 < 5) and (10 == 10) and ("hello" != "world")
# Output: True

print("Question - 13")
x = (2 < 5)
y = (10 == 10)
z = ("hello" != "world")
result = x and y and z
print(result)

# 14. Example: Combining multiple "or" operators
# Input: (7 < 3) or (5 >= 5) or ("apple" == "apple")
# Output: True

print("Question - 14")
x = (7 < 3)
y = (5 >= 5)
z = ("apple" == "apple")
result = x or y or z
print(result)

# 15. Example: Using "not" operator with an expression
# Input: not (10 > 5 and "car" != "car")
# Output: False

print("Question - 15")
x = 10 > 5
y = ("car" != "car")
result = not(x and y)
print(result)

# 16. Example: Using "not" operator with "or" and "and"
# Input: not (5 > 3 or "dog" == "cat" and 7 < 5)
# Output: False

print("Question - 16")
x = 5 > 3
y = ("dog" == "cat")
z = 7 < 5
result1 = y and z
result2 = x or result1
result = not result2
print(result)

# 17. Example: Combining "and" and "or" operators
# Input: (5 > 3 and "apple" != "banana") or (8 == 8 or 6 < 10)
# Output: True

print("Question - 17")
x = 5 > 3
y = "apple" != "banana"
result1 = x and y
z = 8 == 8 
w = 6 < 10
result2 = z or w
print(result1 or result2)

# 18. Example: Combining "or" and "not" operators
# Input: ("apple" == "banana" or not (6 > 10))
# Output: True

print("Question - 18")
x = "apple" == "banana"
y = not (6 > 10)
result = x or y
print(result)

# 19. Example: Complex combination of "and", "or", and "not"
# Input: not (2 < 5 and (7 > 3 or "hello" == "world"))
# Output: False

print("Question - 19 ")
x = 2 < 5
y = 7 > 3
z = "hello" == "world"
result1 = y or z
result = not (x and result1)
print(result)


# 20. Example: Nested use of "and", "or", and "not" operators
# Input: (not (5 > 3) and (10 != 10 or "car" == "car"))
# Output: False

print("Question - 20")
x = not (5 > 3)
y = 10 != 10
z = "car" == "car"
result1 = y or z
result = x and result1
print(result)