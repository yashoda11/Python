# Create a nested loop to print the multiplication table from 1 to 5 (up to 10 times each).
# Expected Input: None
# Expected Output:
# 1  2  3  4  5
# 2  4  6  8  10
# 3  6  9  12  15
# 4  8  12  16  20
# 5  10  15  20  25

for i in range (1, 6) :
    for j in range(1, 6) :
        print(i*j , end = "\t")
    print()
