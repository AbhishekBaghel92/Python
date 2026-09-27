# logical operator
x=int(input("enter x number: "))
y=int(input("enter y number: "))

print(x==10 and x<y)
print(x==10 and x>y)
print(x==5+5 and x*2 and x>y)
print(x==10 and x*2 and x<y)

print(x==10 or x<y)
print(x==5+5 or x>y)
print(x==4 or x*2 or x>y)
print(x==10 or x*2 or x<y)

print(not x==10 )
print (not x!=10)
print(not x!=20)

