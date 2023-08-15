# Write a nested loop that prints a diamond pattern of stars (asterisks).
# Expected Input: None
# Expected Output:
#   *
#  ***
# *****
#  ***
#   *

for i in range(5):
    for j in range(5):
        if abs(i-2) + abs(j-2) <= 2:
            print("*",end = "")
        else :
            print(" ",end = "")
    print()