number=[20,10,30,40,50]
n=[]

for i in (number):
    i = i*2
    n.append(i)
print(n)
for i in range(len(n)):
    for j in range(len(n)-1):
        if n[j] < n[j+1]:
            c=n[j]
            n[j]=n[j+1]
            n[j+1]=c
print(n)
            
    