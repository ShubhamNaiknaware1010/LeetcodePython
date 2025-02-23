# num = int(input("Enter a number"))

# m = num // 3

# n = 3 * m*(m+1) // 2
# print(n)
# sum = 0
# for i in range(0,n + 1,3):
#     sum +=  i
# print(sum)

def getnsum(n,num):
    m = num // n
    nsum = n * m*(m+1) // 2
    return nsum

print(getnsum(3,100))