# Question 7:
# Write a while loop that calculates the factorial of a given number.
# Expected Input: 4
# Expected Output: 24 (4! = 4 * 3 * 2 * 1 = 24)

factorial_Number = int(input("Enter a Number : "))

number = 1 
factorial = 1

while number <= factorial_Number :
    factorial *= number
    number += 1

print("The Factorial of", factorial_Number, "is : ", factorial)
