def isLeapYear(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False

year = int(input("Enter the year "))

for i in range(100):
    if isLeapYear(i):
        print("Leap year",i)
    else:   
        print("Not a leap year",i)
    
