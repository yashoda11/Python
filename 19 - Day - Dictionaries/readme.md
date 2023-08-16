# Dictionaries 

**Dictionaries :**
- Dictionaries are mutable.
- Dictionaries are defined using curly braces `{ }`, and each key-value pair is separated by a colon `:`.

**Creating Dictionaries :**
- We can create a dictionary by enclosing key-value pairs in curly braces.

```# Example: Creating a dictionary of student information
student = {
    "name": "Dodagatta Nihar",
    "age": 25,
    "major": "Computer Science",
    "gpa": 3.8
}
```

**Accessing Values :**
- We can access values in a dictionary using keys. 
- Dictionary keys are unique.

```# Example: Accessing values in a dictionary
student = {
    "name": "Dodagatta Nihar",
    "age": 25,
    "major": "Computer Science",
    "gpa": 3.8
}

print(student["name"])  # Output: "Dodagatta Nihar"
print(student["gpa"])   # Output: 3.8
```