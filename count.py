l=[]
n=int(input("Enter the size of the list:"))

for i in range(n):
    c=int(input())
    l.append(c)
print("The list:",l)
dict1={}
for c in l:
    if c in dict1:
        dict1[c]=dict1[c]+1
    else:
        dict1[c]=1

print(dict1)