
class oddoreven:
    def check(self,num):
          if num%2==0:
                print("even")
          else:
                print("odd")

c=oddoreven()
class inputnum:
    def input(self):
        num=int(input("enter a number:"))
        
        c.check(num)


a=inputnum()
a.input()

    
    