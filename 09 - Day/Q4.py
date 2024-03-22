# **Question 4:**
# Write a program that takes a year as input and prints "Leap Year" if it's a leap year, and "Not a Leap Year" otherwise.
# **Expected Input:** Enter a year: 2024
# **Expected Output:** Leap Year

year = int(input("Enter a Year : "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("Leap Year")
else:
    print("Not a Leap Year")



if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap")
else:
    print("NO L")