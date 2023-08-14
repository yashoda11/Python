# Question 4:
# Create a while loop that keeps prompting the user for a number until they enter a negative number.
# Expected Input: 5, 10, -2
# Expected Output: (No output, just prompt for input)


while True :
    number = int(input("Enter a Number : "))
    if number < 0 :
        break
