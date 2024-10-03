l=[]
def number():
    n=int(input("enter the size:"))
    for i in range(n):
        num=int(input("enter the elements:"))
        l.append(num)
    a=1
    l.sort()
    for num in l:
        if num==a:
            a=a+1
    print("the  misssed num:",a) 
number()           