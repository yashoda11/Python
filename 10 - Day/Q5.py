# Question 5:Check if a given `year` is a leap year, and if it is, find the number of days in February for that year.
# Expected Input:year = 2000
# Expected Output:Leap Year, February has 29 days

year = int(input("Enter a Year : "))

if ( year % 4 ) == 0 :
    if ( year % 100 ) == 0 :
        if ( year % 400 ) == 0 :
            print ("Leap Year, February has 29 days")
        else :
            print ("Not a Leap Year")
    else :
        print("Leap Year, February has 29 days")
else :
    print("Not A Leap Year")