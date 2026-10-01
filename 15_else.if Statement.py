rate = int(input("Enter rate number: "))
qty = int(input("Enter qty number: "))

amt = rate * qty
print("Amount:", amt)

if amt >= 100000:
    d = 15
    dis = amt * d / 100

elif amt >= 50000 and amt <= 99999:
    d = 10
    dis = amt * d / 100

elif amt >= 20000 and amt <= 49999:
    d = 5
    dis = amt * d / 100

else:
    d = 0
    dis = 0

print("Discount:", d, "%", sep="")
print("Discount:", dis)

na = amt - dis
print("Net Amount:", na)