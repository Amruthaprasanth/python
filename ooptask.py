class Calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def divide(self,a,b):
        return a/b
    def option(self):
        while True:
            print("Menu")
            print("1.Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Exit")
            choice = input("Choose an option: ")
            if choice == '5':
                print("Exit")
                break
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))

            if choice == '1':
                    result = self.add(a, b)
                    print(f"The result is: {result}")
            elif choice == '2':
                    result = self.sub(a, b)
                    print(f"The result is: {result}")
            elif choice == '3':
                    result = self.mul(a, b)
                    print(f"The result is: {result}")
            elif choice == '4':
                    result = self.divide(a, b)
                    print(f"The result is: {result}") 
            else:
                    print("Invalid option. Please try again.")
calculator=Calculator()
calculator.option()  
