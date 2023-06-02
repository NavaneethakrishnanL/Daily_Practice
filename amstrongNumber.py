###ARMSTRONG_NUMBER

given_number=int(input("Enter the number: " ))
number = given_number
cube=0
while number!=0:
    mod=number%10
    cube=(mod**3)+cube
    number=number//10
if given_number == cube:
    print("The Number is Amstrong Number")
else:
    print("The Number is not an Amstrong Number")

