number=[20,60,80,10,5]

for i in range((len(number))):
    for j in range(len(number)-1):
        if number[j+1]>(number[j]):
            c=number[j]
            number[j] = number[j+1]
            number[j+1]=c

print(number)


