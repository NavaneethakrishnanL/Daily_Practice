number = int(input())

if number>=0:
    f=1
    for i in range(1,(number+1)):
        f=f*i
        print(f)
    
else:
    print("Invalid Number")

