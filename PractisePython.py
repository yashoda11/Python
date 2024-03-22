# # # # # # # # # # # # # sentence = "Python  ";
# # # # # # # # # # # # # # print(sentence * 3)
# # # # # # # # # # # # # num = input("enter a number : ");
# # # # # # # # # # # # # number = int(num);
# # # # # # # # # # # # # print("specified number (" , number ,  ") times is :" , sentence * number)

# # # # # # # # # # # # a = 6
# # # # # # # # # # # # b = 2
# # # # # # # # # # # # c = 9

# # # # # # # # # # # # print(c//b)

# # # # # # # # # # # value = 2
# # # # # # # # # # # print(value)
# # # # # # # # # # # new_value = input("enter New value : ");
# # # # # # # # # # # value = new_value
# # # # # # # # # # # print("The new V is : ", value)

# # # # # # # # # # a = "hai "

# # # # # # # # # # print(a * 3)

# # # # # # # # # # s = "arrow"
# # # # # # # # # # print("*" * 3, s , "*" * 3)

# # # # # # # # # userIn = "Haiwr"
# # # # # # # # # # print(userIn)
# # # # # # # # # print(len(userIn), userIn[1])

# # # # # # # # # # str1 = input("Enter name : ")
# # # # # # # # # # str2 = input("Enter Gree : ")
# # # # # # # # # # print(str2 + " " + str1)

# # # # # # # # # 5. Example: Get a substring from index 7 to index 14 (exclusive).
# # # # # # # # # Input: "Welcome to Python programming."
# # # # # # # # # Output: " to Pyt"

# # # # # # # # # input = "Welcome to Python programming."
# # # # # # # # # result = input[7:14]
# # # # # # # # # print(result)

# # # # # # # # # 6. Example: Get a substring from index -9 to -3.
# # # # # # # # # Input: "The future is bright."
# # # # # # # # # Output: "s brig"

# # # # # # # number = int(input("Enter a Number : "))

# # # # # # # if number % 2 == 0:
# # # # # # #     print("Even");
# # # # # # # else:
# # # # # # #     print("Odd")

# # # # # # number1 = int(input("NUMBER1 : "))
# # # # # # number2 = int(input("NUMBER2 : "))

# # # # # # if number1 >  number2 :
# # # # # #     print("number1 is greater")
# # # # # # else:
# # # # # #     print("number2 greater")

# # # # # # if number1 >  number2 :
# # # # # #     print(number1)
# # # # # # else:
# # # # # #     print(number2)

# # # # # # x = input("Enetr a Character : ")

# # # # # # if ( x == "a" or x == "e" or x == "i" or x == "o" or x == "u") :
# # # # # #     print("Vowel");
# # # # # # else :
# # # # # #     print("Consonant")

# # # # # def isVowelOrCons(char):
# # # # #     vowels = "aeiouAEIOU"
# # # # #     if char in vowels:
# # # # #         print("Vo")
# # # # #     else:
# # # # #         print("con")

# # # # # character = input("Enter a Character : ")

# # # # # if len(character) == 1 and character.isalpha():
# # # # #     isVowelOrCons(character)
# # # # # else:
# # # # #     print("Invali")


# # # # year = int(input("Enter a Year : "))

# # # # if year % 4 == 0:
# # # #     if year % 100 == 0:
# # # #         if year % 400 == 0:
# # # #             print("Leap Year")
# # # #         else:
# # # #             print("Not a Leap Year")
# # # #     else:
# # # #         print("Leap Year")
# # # # else:
# # # #     print("Not a Leap Year")


# # # # #  OR

# # # # if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
# # # #     print("Leap")
# # # # else:
# # # #     print("NO L")

# # # grade = input("Enter a Grade (A, B, C, D, or F) : ")

# # # if grade == "A" or grade == "B" or grade == "C" or grade == "D" or grade == "a" or grade == "b" or grade == "c" or grade == "d":
# # #     print("Pass")
# # # else :
# # #     print("Fail")


# # def checkGrade(grade):
# #     if grade in ['A', 'B', 'C', 'D']:
# #         print("PASS")
# #     elif grade == 'F':
# #         print("FAIL")
# #     else:
# #         print("Invalid grade")


# # grade = input("Enetr grade : ")

# # checkGrade(grade.upper())

# number = int(input("num : "))

# if number > 0:
#     print("Pos")
# elif number <0:
#     print("neg")
# else:
#     print("Ze")

# if number % 2 == 0 :
#     print("Even Number")
# else:
#     print("Odd Number")


# num = 1

# while num <= 5:
#     print(num)
#     num += 1

# num = 1
# sum = 0

# while num <= 10:
#     sum += num
#     num += 1

# print(sum)

# num = 2

# while num <= 10:
#     print(num)
#     num += 2

# num = 5

# while num >= 1:
#     print(num)
#     num -= 1

# n = 22

# num1, num2 = 0, 1

# while num1 <= n:
#     print(num1)
#     num1, num2 = num2, num1 + num2

# while True:
#     n = int(input("Enter Numbers : "))
#     if n == 10:
#         print("GUESS CORRECT")
#         break



# while True:
#     n = int(input("Enter n : "))
#     if n < 0:
#         print("Negative")
#         break

# sum = 0

# while True:
#     n = int(input("Enter n : "))
#     sum += n
#     n += n
#     if n == 0:
#         break

# print(sum)

# for num in range(1, 6):
#     print(num)

# sum = 0
# for num in range (1, 11) :
#     sum += num
#     num += 1
# print("The Sum of Numbers from 1 to 10 is :", sum)

# print("To print each character in the string 'Hello' is :")
# sequence = "Hello"
# for char in sequence:
#     print(char)


# print("To print the first 10 even numbers :")
# for num in range(0,20) :
#     if num % 2 == 0 :
#         print(num)


# print("Doubles each number in the sequence: 1, 2, 3, 4, 5 :")
# for num in range(1,6) :
#     print (num*2)

# Input: "I love Python programming"
# Expected Output:
# I
# love
# Python
# programming

# string = "I love Python programming"
# splitted = string.split()
# print(splitted)
# for word in splitted :
#     print(word)

# 7. Write a Python program that takes a user input string and replaces all occurrences of "Python" with "Java" using the replace() method.
# Input: "I love Python programming, Python is great."
# Expected Output: "I love Java programming, Java is great."

# str = "I love Python programming, Python is great."
# res = str.replace("Python", "Java")
# print(res)

# str = "I love Python programming, Python is great."
# res = str.startswith("I")
# print(res)

# str = "I love Python programming, Python is great."
# res = str.endswith("great.")
# print(res)

# *****
# *****
# *****
# *****
# *****

# for i in range(5):
#     for j in range(5):
#         print("*", end = "")
#     print()

# 1  2  3  4  5
# 2  4  6  8  10
# 3  6  9  12  15
# 4  8  12  16  20
# 5  10  15  20  25

# for i in range(1, 6):
#     for j in range(1, 6):
#         print(i*j, end = " ")
#     print()

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# for i in range(1, 6):
#     for j in range(i):
#         print(j+1, end = " ")
#     print()



# *****
# *   *
# *   *
# *   *
# *****

# for i in range(5):
#     for j in range(5):
#         if i == 0 or i == 4 or j == 0 or j == 4:
#             print("*", end = "")
#         else:
#             print(" ", end = "")
#     print()


sum = 0

for i in range(1, 11):
    si = 0
    for j in range(1, i+1):
        si+=1
    sum+=si

print(sum)

sum = 0

for i in range(1, 6):
    sum+=i
print(sum)

num = 1
sum = 0

while num <=5:
    sum+=num
    num+=1
print("W", sum)

#  5  4  3  2  1
# 10 8  6  4  2
# 15 12 9  6  3
# 20 16 12 8  4
# 25 20 15 10 5

for i in range(1, 6):
    for j in range(10, 0, -1):
        print(i*j, end = "\t")
    print()

# *
# **
# ***
# ****
# *****

for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

#  *
#  ***
# *****
#  ***
#   *

print("Dia")
for i in range(5):
    for j in range(5):
        if abs(i-2) + abs(j-2) <= 2:
            print("*", end=" ")
        else:
            print(" ", end = " ")
    print()

    # 10. Create a nested loop to find and print the factorial of numbers from 1 to 5.
# Expected Input: None
# Expected Output: 1 2 6 24 120

n = 5
num = 1
fac = 1

while num <= n:
    fac *= num
    num +=1
print(fac)

print("FAC - FOR LOOP")
fac = 1

for i in range(1, 6):
    fac1 = 0
    for j in range(1, i +1):
        fac1 += 1
    fac *= fac1
    print(fac, end = " ")

print()


factorial = 1
for i in range(1, 6):
    factorial *= i
    print(factorial, end = " ")

print("\n\n------------\n")
for num in range(1, 10):
    if num == 5:
        break
    print(num)

