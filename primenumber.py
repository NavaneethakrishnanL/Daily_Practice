number=int(input())


# if (number%number)==0 and(number%1)==0 and ((number%2)!=0 or (number==2)):
#     print("The number is a prime number: ",number)
# else:
#     print ("Not a Prime Number")


# for i in range(1, number+1):
#     if (i%i)==0 and  (i%1)==0 and (((i%2)!=0 or (i==2)) and ((i%3)!=0 or (i==3))):
#         print("The number is a prime number: ",i)
#     else:
#         print ("Not a Prime Number", i)

# for i in range(1,number+1):
for k in range(1,number+1):
    
    div=int(number/2)
    flag=0
    if number>1:

        for i in range(2,div):
            if (number%i)==0:
                flag=1
                # print("Not a Prime number:",i, number)
                break
            else:
                # print("prime number :",i, number)
                flag=0
        if flag==0:
            print('Prime Number')
        else:
            print ('not a prime number')
    else:
        print('not a prime')