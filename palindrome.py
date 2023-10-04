number=int(12332)
print(number)
checkNumber=number

rev=0

while number!=0:
    reminder=number%10
    rev=rev*10+reminder
    number=number//10
print(rev)
if rev==checkNumber:
    print("Plaindrome")
else:
    print("Not a plaindrome!")