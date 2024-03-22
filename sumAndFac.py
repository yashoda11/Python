sum = 0

for num in range(1, 6):
    sum+=num
print(sum)

print("---------")

sum = 0
num = 1

while num<=5:
    sum+=num
    num+=1
print(sum)

print("-----------")


fac = 1
num = 1

while num<=5:
    fac*=num
    num+=1
print(fac)

print("------------")

fac = 1
for num in range(1, 6):
    fac*=num
print(fac, end="\t")

print("\n----------------")

sum=0
for i in range(1, 6):
    si = 0
    for j in range(1, i+1):
        si+=1
    sum+=si 
    print(sum, end="\t")

print("\n---------------")

fac = 1

for i in range(1, 6):
    fac1=0
    for j in range(1, i+1):
        fac1+=1
    fac*=fac1
    print(fac, end="\t")
print(fac)

print("\n\n----------------\n\n")
# 3. Write a Python function that takes a string as input and checks if it contains the letter 'o'. If it does, print "Found 'o'" and use the `break` statement to stop searching.
#     Input: "Hello, World!"
#     Expected Output:
#     Found 'o'

string = "Hello`"

for char in string.upper():
    if 'O' in char:
        print("Found 'o'")
        break
        


# 4. Given a list of numbers [1, 2, 3, 4, 5], use a `for` loop to double each element and print the result. However, if the element is 4, use the `continue` statement to skip it.
# Expected Output:
# 2
# 4
# 6
# 10   

num = [1, 2, 3, 4, 5]

for n in num:
    if n == 4:
        continue
    print(n*2)

print("\n\n----------------\n\n")
# 5. Write a Python program to print all numbers from 1 to 20 using a `while` loop. However, stop the loop when reaching 15 using the `break` statement.
# Expected Output:
# 1
# 2
# 3
# ... (up to 15)

num = 1

while num <=20:
    print(num)
    num+=1
    if num == 16:
        break
    
# string = input("Enter a String : ")
# if string == "  ":
#     print(True)
# else:
#     print(False)

# 3. Write a Python function that takes a list of numbers as input and returns the sum of all the numbers.
# Input: [1, 2, 3, 4, 5]
# Expected Output: 15

names = input("Enter strings with space : ")

listOfnames = [name for name in names.split()]
print(listOfnames)

gname = input("enter iden name : ")
print(gname)

if gname in listOfnames:
    print("Found")
else:
    print("Not Found")

