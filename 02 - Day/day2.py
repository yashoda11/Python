# Questions to Practice (Day - 2):

# 1. Declare two variables `a` and `b`, assign integer values to them, and print their sum.
# **Expected Output:** The sum of `a` and `b`.

a = 10
b = 15
sum = a + b
print("The Sum of", a, "and", b, "is :", a + b)

#2. Create a variable `name` and assign your name to it. Print a greeting message using your name.
# **Expected Output:** Greeting message with your name, e.g., "Hello, John!"

name = "Yashoda!"
print("hello,", name)

#3. Define a variable `pi` and assign the value of π (pi) to it. Print the value of `pi`.
# **Expected Output:** The value of π (pi), e.g., 3.14159.

pi = 3.14159
print("The Value of π (pi) is :",pi)

#4. Define a variable `is_raining` and ask the user to input either "True" or "False" (as a string). Convert the input to a boolean and print its type.
#   - **Expected Input:** "True" or "False"
#   - **Expected Output:** The data type of the converted boolean.

is_raining = input("Is Raining Outside, Enter True or False ?")
is_raining_outside = bool(is_raining)
print(type(is_raining_outside))

#5. Create a string variable `sentence` containing any sentence of your choice. Ask the user to input a number, convert it to an integer, and print the sentence repeated that number of times.
#   - **Expected Input:** A number (e.g., "3")
#   - **Expected Output:** The sentence repeated the specified number of times.

sentence = "I Love Python  "
num_str = input("Enter Specified number :")
num_int = int(num_str)
print("The sentence repeated the specified number of times (",num_int,") is :",sentence * num_int)

# 6. Given two variables `x` and `y`, perform the following operations and print the results:
#     - Addition of `x` and `y`.
#     - Subtraction of `y` from `x`.
#     - Multiplication of `x` and `y`.
#     - Division of `x` by `y`.
#     - `x` raised to the power of `y`.
#     - The remainder when `x` is divided by `y`.
#     - The floor division of `x` by `y`.

# In Python, we can perform floor division (also sometimes known as integer division) using the // operator. This operator will divide the first argument by the second and round the result down to the nearest whole number, making it equivalent to the math.floor() function.

x = 4
y =  2

print("Addition(+) of x and y is :", x + y)
print("Subtraction(-) of x and y is :", x - y)
print("Multiplication(*) of x and y is :", x * y)
print("Division(/) of x and y is :", x / y)
print("Exponentiation(x raised to the power of y) of x and y is :", x ** y)
print("remainder(%) of x and y is :", x % y)
print("Floor Division(//) of x and y is :", x // y)

# 7. Define a variable `value` and assign any numerical value to it. Ask the user to input a new value. Update the variable `value` with the new input and print the updated value.
# - **Expected Input:** A numerical value (e.g., "42")
# - **Expected Output:** The updated value of the variable.

value = 42
print("Initial Value is :", value)
new_value = input("Enter a new numerical Value : ")
value = new_value
print("Updated Value is :", value)