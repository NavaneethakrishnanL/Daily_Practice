ay=[90,3,50,60,1,10]

min= ay[0]
max=ay[0]
for i in (ay):
    if min>i:
        min = i
    if max<i:
        max = i

print(min, max)