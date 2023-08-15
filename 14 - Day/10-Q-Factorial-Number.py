# 10. Create a nested loop to find and print the factorial of numbers from 1 to 5.
# Expected Input: None
# Expected Output: 1 2 6 24 120


factorial = 1
for i in range(1, 6):
    factorial *= i
    print(factorial, end = " ")