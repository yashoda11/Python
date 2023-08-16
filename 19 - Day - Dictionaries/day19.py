# Example: Creating a dictionary of student information

student = {
    "name" : "Yashoda V",
    "age" : 28,
    "major" : "CS",
    "gpa" : 7.5
}
print(student)

# Example: Accessing values in a dictionary
student = {
    "name" : "Yashoda V",
    "age" : 28,
    "major" : "CS",
    "gpa" : 7.5
}

print(student["name"])
print(student["age"])

print("-----------------------------------------------")

### Questions to practice (Day - 19):

# 1. Question: Create an empty dictionary.
# Expected Output: {}

print("Question - 01")
student = {}

print("-----------------------------------------------")

# 2. Question: Create a dictionary to store the age of two people, "John" and "Alice." John is 25 years old, and Alice is 30 years old.
# Expected Output: {"John": 25, "Alice": 30}

print("Question - 02")
persons = {
    "John" : "25",
    "Alice" : "30"
}
print(persons)

print("-----------------------------------------------")

# 3. Question: Access the value associated with the key "city" from the given dictionary.
# Expected Input: Dictionary: {"name": "Alice", "city": "New York", "age": 30}
# Expected Output: "New York"

print("Question - 03")
Dictionary = {
    "name": "Alice", 
    "city": "New York", 
    "age": 30
    }

print(Dictionary["city"])

print("-----------------------------------------------")

# 4. Question: Create a dictionary to store the contact information of a person. The person's name is "Bob," and their email is "[bob@example.com](mailto:bob@example.com)."
# Expected Output: {"name": "Bob", "email": "[bob@example.com](mailto:bob@example.com)"}

print("Question - 04")
contact_information = {
    "name" : "Bob",
    "email" : "bob@example.com"
}
print(contact_information)

print("-----------------------------------------------")

# 5. Question: Access the value associated with the key "score" from the given dictionary.
# Expected Input: Dictionary: {"name": "John", "age": 22, "score": 85}
# Expected Output: 85

print("Question - 05")
Dictionary = {
    "name": "John",
    "age": 22, 
    "score": 85
    }
print(Dictionary["score"])

print("-----------------------------------------------")

# 6. Question: Create a dictionary to represent a rectangle. The rectangle has a width of 10 and a height of 5.
# Expected Output: {"width": 10, "height": 5}

print("Question - 06")
rectangle_dimensions = {
    "width" : 10,
    "height" : 5
}
print(rectangle_dimensions)

print("-----------------------------------------------")

# 7. Question: Access the value associated with the key "phone" from the given dictionary. If the key does not exist, return "Not available."
# Expected Input: Dictionary: {"name": "Eve", "age": 27}
# Expected Output: "Not available"

print("Question - 07")
dictionary = {
    "name": "Eve", 
    "age": 27
    }
value = dictionary.get("phone", "Not Available")
print(value)

print("-----------------------------------------------")