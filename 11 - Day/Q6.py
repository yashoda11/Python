# Question 6:
# Create a while loop that asks the user to guess a secret number (e.g., 7) and continues until the correct number is guessed.
# Expected Output: (Depends on user input)

while True :
    number = int(input("Enter a Secret Number : "))
    if number == 7 :
        print("Your Guess is Correct")
        break