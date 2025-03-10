a,b,c = map(int,input().split())
if a==b and a==c and a==c:
    print("equilateral")
elif a==b or b==c or a==c:
    print("isosceles")
else:
    print("scalene")   