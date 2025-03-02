"""
Given an integer x, return true if x is a palindrome and false otherwise."""

def isPalindrome(num):
    if num < 0:
        return False
    temp = num
    rev = 0
    while(temp > 0):
        rem = temp % 10
        rev = rev * 10  + rem
                                                                  
        temp = temp // 10
    return num == rev


print(isPalindrome(121))