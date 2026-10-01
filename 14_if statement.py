rate=int(input("enter rate number: "))
qty=int(input("enter qty number:"))
amt=rate*qty
print("Amount: ",amt)

if(amt>=100000):
    d=10
    dis=amt*10/100

else:
    d=5
    dis=amt*5/100
    print("discount :",d,"%",sep='')
    print("discount:",dis)
    na=amt-dis
    print("net Amount:",na)   
