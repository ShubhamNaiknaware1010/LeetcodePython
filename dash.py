a = [1,2,3,4,5]
b = [1,2,3,4,5]

c = a

print(a is b)
print(a is c)


a = 10
b = 10
print(a is b)
a = 3
print(a is b)


s = "a" in "abc"
print(s)
s = "a" in "bc"
print(s)

l = [1,3,4,5]

print( 3 in l)          