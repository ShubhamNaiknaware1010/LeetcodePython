# Python Program to print the sum of all multiples of a Number below a given range

def get_sum(n,num):
    m = num // n
    sum = n * m*(m+1) // 2
    return sum

# Enter a number
num = int(input("Enter a number: "))
# Enter the range
end = int(input("Enter the end of the range: "))

print(get_sum(num,end))

