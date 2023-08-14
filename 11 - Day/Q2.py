# Question 2:# Create a while loop that calculates the sum of numbers from 1 to n, where n is the input.
# Expected Input: 5
# Expected Output: 15 (1 + 2 + 3 + 4 + 5)

num = int(input("Enter a Number : "))

number = 1
sum = 0

while number <= num :
    sum += number
    number += 1

print("Sum of Number from 1 to", num, "is : ", sum)