def dissarium():
    num=str(n)
    sum=0
    for i in range(len(num)):
        digit=int(num[i])
        position=i+1
        sum=sum+digit**position

    if n==sum:
        print("its a dissarium num")
    else:
        print("its not dissarium num")    
n=int(input("enter a number:"))
dissarium()











