# Example: Modifying and adding key-value pairs
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

# Example: Dictionary methods
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

print("---------------------------------------------------------------------------")

### Questions to practice (Day - 20):

# 1. Question: Given the initial dictionary `employee` as `{"name": "Alice", "age": 30}`, modify the value of the key "age" to 35.
# Expected Input: `employee = {"name": "Alice", "age": 30}`
# Expected Output: `{"name": "Alice", "age": 35}`

print("Question - 01")
employee = {
    "name": "Alice", 
    "age": 30
    }
print(employee)
print("After modify the value of the key 'age' to 35")
employee["age"] = 35
print(employee)

print("---------------------------------------------------------------------------")

# 2. Question: Add a new key-value pair to the dictionary `fruits`, where the key is "orange" and the value is 3.
# Expected Input: `fruits = {"apple": 5, "banana": 7}`
# Expected Output: `{"apple": 5, "banana": 7, "orange": 3}`

print("Question - 02")
fruits = {
    "apple": 5, 
    "banana": 7
    }
print(fruits)
print("Add a new key-value pair to the dictionary 'fruits'")
fruits["orange"] = 3
print(fruits)

print("---------------------------------------------------------------------------")

# 3. Question: Given the dictionary `inventory`, remove the key "sugar" and its associated value from the dictionary.
# Expected Input: `inventory = {"apple": 10, "banana": 15, "sugar": 2}`
# Expected Output: `{"apple": 10, "banana": 15}`

print("Question - 03")
inventory = {
    "apple": 10, 
    "banana": 15, 
    "sugar": 2
    }
print(inventory)
print("After remove the key 'sugar'' and its associated value from the dictionary :")
remmove_value = inventory.pop("sugar")
print(inventory)

print("---------------------------------------------------------------------------")

# 4. Question: Create a function called `add_stock` that takes a dictionary `stock` and an item `item_name` (string) as input and adds 1 to the value of the corresponding key in the dictionary. Return the modified dictionary.
# Expected Input: `stock = {"apple": 10, "banana": 15}`, `item_name = "banana"`
# Expected Output: `{"apple": 10, "banana": 16}`

print("Question - 4")
def add_stock(stock, item_name) :
    if item_name in stock :
        stock[item_name] += 1
    return stock

stock = {
    "apple": 10, 
    "banana": 15
    }
item_name = "banana"
print("stock :", stock)
print("item_name :", item_name)
print("After Updating : ")
updated_stock = add_stock(stock, item_name)
print(updated_stock)

print("---------------------------------------------------------------------------")

# 5. Question: Given the dictionary `scores`, check if the key "Alice" exists. If it exists, print the associated value; otherwise, print "Key not found."
# Expected Input: `scores = {"Bob": 85, "Charlie": 90, "Alice": 78}`
# Expected Output: `78`

print("Question - 05")
scores = {
    "Bob": 85, 
    "Charlie": 90, 
    "Alice": 78
    }
value = scores.get("Alice", "Key not found")
print(value)

print("---------------------------------------------------------------------------")

# 6. Question: Write a function called `count_vowels` that takes a string `text` as input and returns a dictionary containing the count of each vowel (a, e, i, o, u) in the text. Ignore case sensitivity.
# Expected Input: `text = "Hello, World!"`
# Expected Output: `{"a": 0, "e": 1, "i": 0, "o": 2, "u": 0}`

print("Question - 06")
def count_vowels(text):

    vowels = "aeiou"
    vowels_count = {'a' : 0, 'e' : 0, 'i' : 0, 'o' : 0, 'u' : 0}

    for char in text :
        char_lower = char.lower()
        if char_lower in vowels:
            vowels_count[char_lower] += 1
    return vowels_count

text = "Hello World!"
result = count_vowels(text)
print(result)

print("---------------------------------------------------------------------------")

# 7. Question: Given the dictionary `student_grades`, find the highest grade and its corresponding student name. The dictionary contains student names as keys and their grades as values.
# Expected Input: `student_grades = {"Alice": 85, "Bob": 90, "Charlie": 78}`
# Expected Output: `("Bob", 90)`

print("Question - 07")
student_grades = {
    "Alice": 85, 
    "Bob": 90, 
    "Charlie": 78
    }
    
highest_grade = max(student_grades.items(), key=lambda x: x[1])
print(highest_grade)