# Question 1: Check if a given number `num` is positive, negative, or zero.
# Expected Input: num = 8
# Expected Output: Positive

number = int(input("Enter a Number : "))

if number > 0 :
    print("Entered Number", number, "is a Positive Number")
elif number < 0 :
    print("Entered Number", number, "is a Negative Number")
else :
    print("Enter Number is Zero")