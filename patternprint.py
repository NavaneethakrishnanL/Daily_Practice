number =int(input())

mylist=[]
for i in range(1,number+1):
    mylist.append("*"*i)

    if i==number and (i!=0):
        for j in reversed(range (number)):
            mylist.append("*"*(j))
print("\n".join(mylist))