Input=int(input())
a = [0,1]

print(a)
i=2
for i in range(2,Input):
    a.append(a[i-2]+a[i-1])
    print(a[i])
    