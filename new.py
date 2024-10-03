users=[]
def user_fun():
    while True:
        print("User Menu")
        print("1.Registration")
        print("2.Login")
        print("3.Exit")
        choice= input("Select a choice: ")
        if choice=='1':
         register()
        elif choice== '2':
         login()
        elif choice=='3':
            print("exit")
            break
        else:
            print("Invalid")
def register():
   name=input("eneter your name: ")
   age=int(input("enter age:"))
   address=input("enter adress:")
   phone=input("enter phone:")
   username=input("enter username:")
   for user in users:
    if user['username'] ==username :
      print("Username already exists")
   password=input("enter password:")
   users.append({'name': name,'age': int(age),'address': address,'phone_number': phone,'username': username,'password': password  })
   print("registration succedssful")
def login():
    username =input("Enter username: ")
    password =input("Enter  password: ")
    for user in users:
        if (user['username']==username and user['password']==password):
            print("Login successful")
user_fun()