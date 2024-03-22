# 5. Write a nested loop to calculate and print the sum of numbers from 1 to 5 using nested iteration.
# Expected Input: None
# Expected Output: 15

sum = 0
for i in range (1,6):
    sum +=i
print(sum)


sum = 0

for i in range(1, 11):
    si = 0
    for j in range(1, i+1):
        si+=1
    sum+=si

print(sum)