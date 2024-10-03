# a="ABA"
# dic = {x: {y: x + y for y in a} for x in a} 
# print(dic)

# dictionary comprehnsion
# keys = ['a','b','c','d','e']
# values = [1,2,3,4,5]  

# myDict = { k:v for (k,v) in zip(keys, values)}  

 
# print (myDict)

# a = {x.upper(): x*3 for x in 'coding '}
# print (a)

# newdict = {x: x**3 for x in range(10) if x**3 % 4 == 0}
# print(newdict)

# print only first letter in a string using list comprehnsion

# li=[]
# size=int(input("enter size of the list: "))
# for i in range(size):
#     s=input("enter the string: ")
#     li.append(s)
# li=[s[0] for s in li ]
# print(li)

# li=[]
# size=int(input("enter size of the list: "))
# for i in range(size):
#     s=input("enter the string: ")
#     li.append(s)
# f=[]
# for s in range(li):
#     f.append(s[0])
# print(f)

# num=[x for x in range(1,51) if x%3==0 and x%5==0]
# print(num)

# string=input("enter a string")
# vowels={x for x in string if x in 'aeiouAEIOU'}
# print(vowels)

# odd={x**2 for x in range(1,15) if x%2!=0}
# print(odd)

# fruits={x:len(x) for x in ['apple', 'banana', 'cherry', 'date']}
# print(fruits)

# even={num:(num %2==0) for num in range(1,11)}
# print(even)

# break

# for string in "python loops":
#     if string=="o" or string=="p" or string=="t":
#         continue
#     print('current letter:',string)

# continue

# for string in "python loops":
#     if string=='l':
#         break
#     print("current letter:",string)

# for string in "python loops":
#     pass
# print('last letter:',string)



        

    
