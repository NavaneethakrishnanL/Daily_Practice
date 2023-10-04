numbers=[1,2,3,4,5,6,7,8,9,10]

odd_numbers=[]
for number in numbers:
    if (number%2) !=0:
        print(number)
        #del numbers[number]
        #numbers = numbers.remove(number)
        odd_numbers.append(number)
numbers=list(set(numbers)-set(odd_numbers))
print(numbers,odd_numbers)


number_factorial=int(input())
i=1
f=1
while i<= number_factorial:
    f=f*i
    i+=1

print(f)

