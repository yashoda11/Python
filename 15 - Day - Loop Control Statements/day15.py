# Example: Using 'break' to stop the loop when the value reaches 3
for num in range(1, 6):
    if num == 3:
        break
    print(num)

print("-----------------------")

# Example: Using 'continue' to skip printing even numbers
for num in range(1, 6):
    if num % 2 == 0:
        continue
    print(num)

print("-----------------------")

# Example: Using 'pass' to do nothing inside the loop
for num in range(1, 6):
    pass

### Questions to practice (Day - 15):

# 1. Write a Python program to print all numbers from 1 to 10, but stop the loop immediately when reaching 5 using the `break` statement.
# Expected Output:
# 1
# 2
# 3
# 4

print("Question - 01")
for i in range(1,6):
    if i == 5:
        break
    print(i)

print("-----------------------")

# 2. Given a list of numbers [1, 2, 3, 4, 5], use a `for` loop to print the elements one by one. However, if the element is 3, skip it using the `continue` statement.
# Note: Mowa nuv ee problem lo list ni create cheyyali ante my_list = [1,2,3,4,5] ani raayi, in detailed lists gurinchi further reels lo maatladta.
# Expected Output:
# 1
# 2
# 4
# 5

print("Question - 02")
my_list = [1, 2, 3, 4, 5]
for num in my_list:
    if num == 3:
        continue
    print(num)

print("-----------------------")

# 3. Write a Python function that takes a string as input and checks if it contains the letter 'o'. If it does, print "Found 'o'" and use the `break` statement to stop searching.
#     Input: "Hello, World!"
#     Expected Output:
#     Found 'o'

print("Question - 03")
while True:
    string = input("Enter a String :")
    if 'o' in string or 'O' in string:
        print("Found 'o'")
        break

print("-----------------------")

# 4. Given a list of numbers [1, 2, 3, 4, 5], use a `for` loop to double each element and print the result. However, if the element is 4, use the `continue` statement to skip it.
# Expected Output:
# 2
# 4
# 6
# 10    

print("Question - 04")
my_list = [1, 2, 3, 4, 5]
for num in my_list:
    if num == 4:
        continue
    print(num*2)

print("-----------------------")

# 5. Write a Python program to print all numbers from 1 to 20 using a `while` loop. However, stop the loop when reaching 15 using the `break` statement.
# Expected Output:
# 1
# 2
# 3
# ... (up to 15)

print("Question - 05")
num = 1
while num <= 20 :
    if num == 16:
        break
    print(num)
    num +=1

