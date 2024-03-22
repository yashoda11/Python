# **Question 3:**
# Write a program that takes a character as input and prints "Vowel" if it's a vowel (a, e, i, o, u), and "Consonant" otherwise.
# **Expected Input:** 
# Enter a character : a
# **Expected Output:** Vowel

x = input("Enetr a Character : ")

if ( x == "a" or x == "e" or x == "i" or x == "o" or x == "u") :
    print("Vowel");
else :
    print("Consonant")



def isVowelOrCons(char):
    vowels = "aeiouAEIOU"
    if char in vowels:
        print("Vowel")
    else:
        print("consonant")

character = input("Enter a Character : ")

if len(character) == 1 and character.isalpha():
    isVowelOrCons(character)
else:
    print("Invalid")