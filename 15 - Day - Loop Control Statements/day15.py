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
