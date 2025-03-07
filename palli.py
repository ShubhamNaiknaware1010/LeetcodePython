s = "ram-mar"

left = 0
right = len(s) - 1
palindrome = True
while(left  < right):
    if s[right] != s[left]:
        palindrome = False
if palindrome:
    print("Palindrome")
else:
    print("Not Palindrome")