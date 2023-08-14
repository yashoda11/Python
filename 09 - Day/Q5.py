# **Question 5:**
# Write a program that takes a grade as input (A, B, C, D, or F) and prints "Pass" if it's A, B, C, or D, and "Fail" if it's F.
# **Expected Input:** Enter your grade: C
# **Expected Output:** Pass

grade = input("Enter a Grade (A, B, C, D, or F) : ")

if grade == "A" or grade == "B" or grade == "C" or grade == "D" or grade == "a" or grade == "b" or grade == "c" or grade == "d":
    print("Pass")
else :
    print("Fail")