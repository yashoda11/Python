# Question 2: Determine the type of a given number `num`: even or odd, and whether it is positive or negative.
# Expected Input:num = -5
# Expected Output: Negative  Odd

number = int(input("Enter a Number : "))

if number > 0 :
    print("Positive ")
elif number == 0 :
    print("Zero")
else :
    print("Negative")

if number % 2 == 0 :
    print("Even Number")
else:
    print("Odd Number")