number=[22,12,32,43,1,2,65,9,11]

for i in range(len(number)):
    for j in range (len(number)-1):
        if number[j]>number[j+1]:
            c=number[j]
            number[j]=number[j+1]
            number[j+1]=c
print(number)