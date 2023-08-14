# Question 3: Classify a given `age` into four categories: baby, child, teenager, or adult.
# Expected Input: age = 16
# Expected Output:Teenager

age = int(input("Enter Age : "))

if age >= 25 :
    print("Adult")
elif age >= 13 :
    print("Teenager")
elif age >= 5 :
    print("Child")
elif age >0 :
    print("Baby")
else :
    print("Invaild Number")