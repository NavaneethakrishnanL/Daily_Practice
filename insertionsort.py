number=[5,11,12,13,6]

for i in range(1,len(number)):
    key = number[i]
    new=i-1
    while number[new]>key and new>=0:
        number[new+1]=number[new]
        new=new-1
    number[new+1]=key
print(number)
