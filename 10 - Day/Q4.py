# Question 4:Assign a grade to a given `percentage`, considering the following grade scale: A (90-100), B (80-89), C (70-79), D (60-69), and F (below 60).
# Expected Input:percentage = 78
# Expected Output:Grade: C

percentage = int(input("Enter a Percentage : "))

if (percentage >= 90) and (percentage <= 100) :
    print("Grade A")
elif (percentage >= 80) and (percentage <= 89) :
    print("Grade B")
elif (percentage >= 70) and (percentage <= 79) :
    print("Grade C")
elif (percentage >= 60) and (percentage <= 69) :
    print("Grade D")
elif percentage <= 60 :
    print("Grade F")
else:
    print("Invailed Number")
