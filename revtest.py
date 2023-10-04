num=int(input())
rev=0
rem = 0
while num != 0:
    rem=num%10
    rev=rev * 10 + rem
    num =int(num/10)
print(rev)
