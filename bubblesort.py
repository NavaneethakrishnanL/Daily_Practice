ay=[90,3,50,60,1,10]

for i in range(0, len(ay)+1):
    for j in range(0,len(ay)-1):
        if ay[j]<ay[j+1]:
            c=ay[j]
            ay[j]=ay[j+1]
            ay[j+1]=c
print(ay)