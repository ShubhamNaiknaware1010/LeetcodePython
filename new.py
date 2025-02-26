# FIXME : Check if the number is odd or even
num = int(input("Enter a number: "))
ans = num & 1
if ans == 1:
    print("Odd")
else:   
    print("Even")


# using OR

ans = num | 1
if ans == num:
    print("Odd")
else:   
    print("Even")