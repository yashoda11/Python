# Create a nested loop that prints a hollow square pattern of stars (asterisks).
# Expected Input: None
# Expected Output:
# *****
# *   *
# *   *
# *   *
# *****

for i in range(5) :
    for j in range(5) :
        if i == 0 or i == 4 or j==0 or j==4 :
            print("*", end = "")
        else :
            print(" ", end = "")
    print()