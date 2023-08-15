# Write a nested loop that prints a right-angled triangle of stars (asterisks).
# Expected Input: None
# Expected Output:
# *
# **
# ***
# ****
# *****

for i in range (1,6):
    for j in range (i):
        print("*", end="")
    print()