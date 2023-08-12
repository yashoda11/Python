# Question - 01 :
# Write a program that takes a number as input and prints "Even" if it's an even number, and "Odd" if it's an odd number.
# Expected Input : Enter a number: 7
# Expected Output : Odd

number = int(input("Enter a Number : "))

if number % 2 == 0:
    print("Entered Number" , number, "is a Even Number")
else :
    print("Entered Number" , number, "is a Odd Number")