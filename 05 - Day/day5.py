# ****Questions to practice (Day - 5)****
num_string = "123"
print(type(num_string))
num_int = int(num_string)
print(type(num_int))

num_float = 3.14
num_int = int(num_float) 
print(num_int)
print(type(num_int))

num_int = 123
print(type(num_int)) # Output: <class 'int'>
num_string = str(num_int)
print(num_string) # Output: 123
print(type(num_string)) # Output: <class 'str'>


num_float = 3.14
print(type(num_float)) # Output: <class 'float'>
num_string = str(num_float)
print(num_string) # Output: 3.14
print(type(num_string)) # Output: <class 'str'>

# Question 1 :  Convert the integer 42 to a string.
# Expected Input:  value = 42
# Expected Output:  result = "42"

value = 42
print("Value is :",value, "and its Data Type is :", type(value))
reslut = str(value)
print("String is :",reslut, "and its Data Type is :", type(reslut))

# Question 2:  Convert the string "123" to an integer.
# Expected Input:  value = "123"
# Expected Output:  result = 123

value = "123"
print("The String is :", value, "and its Data Type is :",type(value))
result = int(value)
print("The Value is :", result, "and its Data Type is :",type(result))

# Question 3:  Convert the float 3.14 to an integer.
# Expected Input: value = 3.14
# Expected Output : result = 3

value = 3.14
print("The Value is :", value, "and its Data type is :",type(value))
result = int(value)
print("The Value is :", result, "and its Data type is :",type(result))

# Question 4 : Convert the string "5.5" to a floating-point number.
# Expected Input : value = "5.5"
# Expected Output : result = 5.5

value = "5.5"
print("The String is :",value, "and its Data Type is : ", type(value))
result = float(value)
print("The value is :",result, "and its Data Type is : ", type(result))

# Question 5 : Convert the integer 100 to a boolean.
# Expected Input : value = 100
# Expected Output : result = True

value = 100
print("The Value is : ", value , "and its Data Type is : ", type(value))
result = bool(value)
print("The Value is : ", result , "and its Data Type is : ", type(result))

# Question 6 : Convert the boolean True to an integer.
# Expected Input : value = True
# Expected Output : result = 1

value = True
print("The Value is :", value, "and its Data Type is :", type(value))
result = int(value)
print("The Value is :", result, "and its Data Type is :", type(result))

# Question 7 : Convert the string `"False"` to a boolean.
# Expected Input : value = “False”
# Expected Output : result = True

value = "False"
print("The String is : ",value, "and its Data Type is :", type(value))
result = bool(value)
print("The Value is : ",result, "and its Data Type is :", type(result))