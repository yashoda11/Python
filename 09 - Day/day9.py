# Example 1: Using 'if' to check a condition
age = 18

if age >= 18:
    print("You are an adult.")

# Example 2: Using 'if' and 'else' to check a condition
age = 15

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Example 3: Using 'if', 'elif', and 'else' to check multiple conditions
age = 25

if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
