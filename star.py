# n=5
# for i in range(n):
#     for j in range(n):
#         print("* ",end="")
#     print()
# left angle triangle

# n=5
# for i in range(n):
#     for j in range(i+1):
#             print("* ",end="")
#     print()

# inverted left triangle
n=5
# for i in range(n-1):
#     for j in range(n-i-1):
#             print("* ",end="")
#     print()
#  right triangle
# for i in range(n):
#     for j in range(n-i):
#         print("  ",end="")
#     for k in range(i):
#             print("* ",end="")
#     print()
#  inverted left triangle

# for i in range(n):
#      for j in range(n-i):
#         print("* ",end="")   
#      for k in range(i):
#              print("  ",end="")
#      print()

# pyramid
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(i):
#             print("* ",end="")
#     print()

# inverted pyramid

# for i in range(n):
#     for j in range(i):
#         print(" ",end="")
#     for k in range(n-i):
#             print("* ",end="")
#     print()

# n = 4

# diamond
n=5
# for i in range(n):
#     for j in range(n-i-1):
#         print("  ",end="")
#     for j in range(i+1):
#         print("*   ",end="")
#     print()
# for i in range(n):
#     for j in range(i+1):
#         print("  ",end="")
#     for j in range(n-i-1):
#         print("*   ",end="")
#     print()

# hollow square

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i == 1 or i == n or j == 1 or j == n:
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print()

# hollow diamond

# for i in range(n):
    
#     for j in range(n-i-1):
#         print(" ", end=" ")
    
#     for k in range(i+1):
#         if k == 0 or k == i:
#             print(" * ", end=" ")
#         else:
#             print("   ", end=" ")
    
#     print()

# for i in range(n):
    
#     for j in range(i+1):
#         print(" ", end=" ")
    
#     for k in range(n-i-1):
#         if k == 0 or k==n-2-i:
#             print(" * ", end=" ")
#         else:
#             print("   ", end=" ")
    
#     print()


# hollow pyramid

# for i in range(n):
#     for j in range(n - i):
#         print(" ", end="")

#     for k in range(2 * i + 1):
#         if k == 0 or k == 2 * i or i == n - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
    
#     print() 

# hour glass

# for i in range(n):
#     for j in range(i):
#         print(" ",end="")
    
#     for k in range(n-i):
#         print("* ", end="")
#     print()


# for i in range(n-1):
    
#     for j in range(n-i-2):
#         print(" ",end="")
    
    
#     for k in range(i+2):
#         print("* ", end="")
#     print() 

# number triangle
# n = 6 
# b = 1 

# for i in range(n):
#     for j in range(i + 1):
#         print(b, end=" ")
#         b += 1
#     print() 
#  rhombus
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end="")
#     for j in range(n):
#         print("*",end=" ")
#     print()
# z pattern
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==4 or j==n-i-1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

# n = 7
# b = 1 

# for i in range(n):
#     for j in range(i + 1):
#         print(b, end=" ")
#         b=b+1
#     b=b-i
#     print() 
# butterfly pattern

n = 5


# for i in range(1, n + 1):
#     # Print left side stars
#     for j in range(i):
#         print("*", end="")
    
#     # Print spaces in the middle
#     for j in range(2 * (n - i)):
#         print(" ", end="")
    
#     # Print right side stars
#     for j in range(i):
#         print("*", end="")
    
#     print()
# for i in range(n, 0, -1):
#     for j in range(i):
#         print("*", end="")
#     for j in range(2 * (n - i)):
#         print(" ", end="")  
#     for j in range(i):
#         print("*", end="") 
#     print()

# hollow left triangle
# n = 5
# for i in range(n):
#     for j in range(i + 1):
#         if j == 0 or j == i or i == n - 1:
#             print("* ", end="")
#         else:
#             print("  ", end="")  
#     print() 

# number pyramid
# n = 5
# for i in range(1, n + 1):
#     
#     for j in range(n - i):
#         print(" ", end="")       
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()