# def count_vowels(s):
#     vowels={'a','e','i','o','u','A','E','I','O','U'}
#     count=0
#     for i in s:
#         if i in vowels:
#             count=count+1
#     return count   
# s=input("enter a sytring ")         
# print(count_vowels(s))

# def anagram(s1, s2):
#     if len(s1) != len(s2) or sorted(s1) != sorted(s2):
#         return "not anagrams"
#     return "are anagrams"
# str1 = input("Enter a string: ")
# str2 = input("Enter a string: ")
# res=anagram(str1, str2)
# print(res)

# def fibonacci(n):

#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1)+fibonacci(n - 2)
# n = int(input("Enter a number: "))
# result = fibonacci(n)
# print(result)
# n=int(input("enter a number:"))
# def fun(n):
#         if n==0:
#             return 0
#         else:
#             return(n+fun(n-1))
# print(fun(n))

# def sum_list(lst):
#     return sum(lst)
# l=[1,2,3,4,5]
# print(sum_list(l))

# def count_words(sentence):
#    words=sentence.split()
#    return len(words)
# sentence=input("enter a string: ")
# res=count_words(sentence)
# print(res)
# n=int(input("enter the number:"))
def armstrong(n):
    a=n
    num=len(str(n))
    b=str(n)

    sum=0
    for i in b:
        print(i)
        sum=sum+int(i)**num
    if(n==sum):
         print("is an Armstrong number")
    else:
        print("is not an Armstrong number")
n = int(input("Enter a number: "))
armstrong(n)

