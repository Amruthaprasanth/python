# languages = ['Python', 'Swift', 'C++']
# languages[2] = 'C'
# print(languages) 
# prime_numbers=[2,3,5,7]
# removed_element=prime_numbers.pop(2)
# print('removed element:',removed_element)
# print('updated list:',prime_numbers)
# languages=['python','swift','c++','c','java','rust','R']

# del languages[1]
# print(languages)
# del languages[-1]
# print(languages)
# del languages[0:2]
# print(languages)

# languages = ['Python','Swift','C++','C','Java','Rust','R']
# languages.remove('Python')
# print(languages) # ['Swift','C++','C','Java','Rust','R’]

# prime_numbers=[2,3,5,7]
# prime_numbers.reverse()
# print('reversed list:',prime_numbers)

# list1=[12,14,16,18,20]
# l=list1*2
# print(l)

# list1=[12,14,16,18,20]
# list2=[9,10,32,54,86]
# l=list1+list2
# print('concatenated list',l)

# list1=[12,14,16,18,20,23,27,39,40]
# a=len(list1)
# print('length of the list',a)

# list1=[12,14,16,39,40]
# for i in list1:
#     print(i)

# list1=[100,200,300,400,500]
# print(600 in list1)
# print(700 in list1)

# list1=[103,675,321,782,200]
# print(max(list1))

# list1=[103,675,321,782,200]
# print(min(list1))

# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
# intersection1 = set(list1).intersection(list2)
# print(intersection1)

# intersection2 = set(list1) & set(list2)
# print(intersection2) 

# a=set()  # empty set
# print(type(a))

# set1={1,6,4,'abc'}
# print(type(set1))

# Days=set(["Monday","Tuesday","Wednesday","Thursday"])
# print(Days)
# print(type(Days))
# for i in Days:
#     print(i)

# Months=set(["January","February","March","April", "May","June"])
# print(Months)
# Months.add("July")

# Months=set(["January","February","March","April", "May","June"])
# print(Months)
# Months.update(["July","August"])
# print(Months)

# months=set(["January","February","March"]) 
# print(months)
# months.discard("January")
# print(months)

# months=set(["January","February","March","April"])      
# print(months)
# months.remove("January")
# print(months)

# Days1={"Monday","Tuesday","Wednesday","Thursday"}
# Days2={"Friday","Saturday","Sunday"}
# print(Days1|Days2)  

# Days1={"Monday","Tuesday","Wednesday","Thursday"}
# Days2={"Monday","Tuesday","Sunday","Friday"}
# print(Days1&Days2)

# Days1={"Monday","Tuesday","Wednesday","Thursday"}
# Days2={"Monday","Tuesday"}
# Days3={"Monday","Tuesday","Friday"}
# print(Days1>Days2)
# print(Days1<Days2)
# print(Days2==Days3)

# Tuple_data=(0,1,2,3,2,3,1,3,2)
# Print(Tuple_data)

# letters =("p", "r", "o", "g", "r", "a", "m", "i", "z")
# print(letters[0])
# print(letters[5])

# letters = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
# print(letters[-1]) 
# print(letters[-3])

# tuple_=('Python',"Tuples")
# print("Original tuple is:",tuple_)
# tuple_=tuple_*3
# print("New tuple is:",tuple_)

# languages = ('Python', 'Swift', 'C++')
# print(C in languages)
# print(Python in languages)


# new_tuple = ('a', 'b', 'c', 'd')
# my_list = list(new_tuple)
# my_list[1] = 'z'
# new_tuple = tuple(my_list)
# print(new_tuple)

# set1 ={1,2,3,4}
# set2 ={3,4,5,6}
# union_set = set1.union(set2)
# intersection_set = set1.intersection(set2)
# print("Union:", union_set)
# print("Intersection:", intersection_set)

# person = {'name': 'John','age': 25,'city': 'New York'}
# person['age']=30
# person['job']='Engineer'
# print(person)

# list1 = [1, 2, 3, 4, 5]
# new_tuple = tuple(list1)
# print(new_tuple)

# d1={'x':10,'y':20}
# d2={'y':30}
# d1.update(d2)
# print(d1)

# choice=int(input("1.addition 2.substraction 3.multiplication 3.division"))
# if choice=='1':
#         num1 = int(input("Enter first number: "))
#         num2 = int(input("Enter second number: "))
#         print(num1,"+",num2,"=",num1+num2)
# elif choice=='2':
#         num1 = int(input("Enter first number: "))
#         num2 = int(input("Enter second number: "))
#         print(f"{num1}-{num2}:",num1-num2)
# elif choice=='3':
#         num1 = int(input("Enter first number: "))
#         num2 = int(input("Enter second number: "))
#         print(f"{num1}*{num2}:",num1*num2)
# elif choice=='4':2
#         num1 = int(input("Enter first number: "))
#         num2 = int(input("Enter second number: "))
#         print(f"{num1}/{num2}:",num1/num2)
# else:
#         print("Invalid choice")

# num=int(input("enter the number to find  odd or even\n"))
# if num%2==0:
#     print("the num is even")
# else:
#     print("the num is odd")
 
# string=input("enter a string")
# rev_string=string[::-1]
# if(rev_string==string):
#     print("the entered string is palindrome")
# else:
#     print("string is not palindrome")

# string=input("enter a string")
# if(('a' in string) or ('e' in string)or('i' in string)or('o' in string)or('u'in string)):
#     print("vowels found")
# else:
#     print("vowels not found")

# num=int(input("enter a number to find its positive or negetive\n"))
# if num>0:
#     print("The number is positive.")
# elif num<0:
#     print("The number is negative.") 
# else:
#     print("the number is zero")   
   
# unit=float(input("enter the unit consumed"))
# cost=0
# if(unit<=100):
#     cost=unit*5
# elif(unit<=200):
#     cost=100*5+(unit-100)*10
# else:
#      cost=100*5+100*10+(unit-200)*15
# print("total bill",cost) 



# mark=float(input("enter the mark of student"))
# if (mark>90):
#     grade="A+"
# elif (mark>=80):
#     grade="A"
# elif (mark>=70):
#     grade="B+"
# elif (mark>=60):
#     grade="B"
# elif (mark>=50):
#     grade="C+"
# elif (mark>=40):
#     grade="C"
# else:
#     grade="Fail"    
#     print("the grade is",grade)

# ch=input("enter the alphabet")
# if ch in ('a','i','e','o','u','A','E','O','U'):
#     print(ch,"is a vowel")
# else:
#     print(ch,"is a consonant")


# year=int(input("enter a year:"))
# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print("the year is leap year")
#         else:
#             print("its not leap year")
#     else:
#             print("is a leap year")
# else:
#     print("its not leap year")

# print((int(input("enter the first number:")))**int(input("enter the second number:"))) #single line power calculation

# height=float(input("Enter your height in meters: "))
# weight=float(input("Enter your weight in kilogram: "))
# BMI=weight/(height*height)
# print("BMI is:",BMI)
# if(BMI>0 and BMI<18.5):
#     print("Underweight")
# elif(BMI>=18.5 and BMI<24.9):
#     print("Normal weight")
# elif(BMI>=30):
#     print("Obese")
# else:
#     print("Invalid weight")

# print(list(range (5,25,4)))
# for i  in range(10):
#     print(i)
# str=input("enter a string")
# l=len(str)
# rev=""
# for i in range(len(str)):
#     print(str[i])
#     rev=str[i]+rev
#     print(rev)

d1={}
size=input("enter the persons want to create")
for i in range(size):
    d2={}
    n=input("enter name:")
    age= int(input("enter age"))
    salary=float(input("eneter salry"))
    city=input("enter city")
    d2["name"]=n
    d2["age"]=age
    d2["salary"]=salary
    d1[i+1]=d2
print(d1)    

