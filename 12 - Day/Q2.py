# 2. Use a for loop to calculate the sum of numbers from 1 to 10.
# Input: None
# Expected Output:
# 55

sum = 0
for num in range (1, 11) :
    sum += num
    num += 1
print("The Sum of Numbers from 1 to 10 is :", sum)