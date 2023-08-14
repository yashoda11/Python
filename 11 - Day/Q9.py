# Question 9 : # Write a while loop that reads numbers from the user until they enter the number 0. Then, it prints the sum of all the entered numbers.
# Expected Input: 3, 5, 2, 0
# Expected Output: 10 (3 + 5 + 2)

sum = 0

while True :
    number = int(input("Enter a Number : "))
    sum += number
    number += number
    if number == 0:
        break
print("The Sum is :", sum)

    