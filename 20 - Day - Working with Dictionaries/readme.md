# Working with Dictionaries

**Working with Dictionaries :**

```# Example: Modifying and adding key-value pairs
student = {
    "name": "Dodagatta Nihar",
    "age": 25,
    "major": "Computer Science",
    "gpa": 3.8
}

# Modifying value
student["gpa"] = 4.0

# Adding new key-value pair
student["university"] = "XYZ University"

print(student)
# Output: {'name': 'Dodagatta Nihar', 'age': 25, 'major': 'Computer Science', 'gpa': 4.0, 'university': 'XYZ University'}
```

**Dictionary Methods :**
- Python provides various built-in methods to perform common operations on dictionaries.

```# Example: Dictionary methods
student = {
    "name": "Dodagatta Nihar",
    "age": 25,
    "major": "Computer Science",
    "gpa": 3.8
}

# Get keys and values
keys = student.keys()
values = student.values()

print(keys)   # Output: dict_keys(['name', 'age', 'major', 'gpa'])
print(values) # Output: dict_values(['Dodagatta Nihar', 25, 'Computer Science', 3.8])

# Check if a key exists in the dictionary
if "major" in student:
    print("Major:", student["major"])  # Output: Major: Computer Science

# Remove a key-value pair from the dictionary
removed_value = student.pop("age")
print("Removed Value:", removed_value)  # Output: Removed Value: 25

print(student)  # Output: {'name': 'Dodagatta Nihar', 'major': 'Computer Science', 'gpa': 3.8}
```