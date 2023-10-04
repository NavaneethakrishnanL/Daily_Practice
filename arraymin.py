number=int(input())
min=[]
for i in range(0,number+1):
    min.append(i)
    min.sort()
print("smallest number", min[0])
print("Max number", min[-1])

