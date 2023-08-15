# 1. Write a for loop to print the first 10 even numbers.
# Input: None
# Expected Output:
# 0
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18

print("To print the first 10 even numbers :")
for num in range(0,20) :
    if num % 2 == 0 :
        print(num)
    