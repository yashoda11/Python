# Create a nested loop to print the reverse of the multiplication table from 1 to 5 (up to 10 times each).
# Expected Input: None
# Expected Output:    
# 5  4  3  2  1
# 10 8  6  4  2
# 15 12 9  6  3
# 20 16 12 8  4
# 25 20 15 10 5

for i in range (1,6):
    for j in range (5,0,-1) :
        print(i*j, end="\t")
    print()

