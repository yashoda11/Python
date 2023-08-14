# Question 8 : Create a while loop that prints the Fibonacci series up to n.
# Expected Input: 10
# Expected Output:
# 0
# 1
# 1
# 2
# 3
# 5
# 8


num1, num2 = 0 , 1

while num1 <= 10 :
    print(num1)
    num1, num2 = num2 , num1 + num2
    