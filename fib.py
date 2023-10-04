Input=int(input())
a=[0,1]

i=2

for i in range(2, (Input+1)):
    a.append((a[i-2]))+(a[i-1])
    print(a)