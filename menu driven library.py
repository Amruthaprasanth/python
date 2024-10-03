admin_credentials = {'admin':'password'}
book={}

def main_menu():
    while True:
        print("MAIN MENU")
        print("1.Admin")
        print("2.User")
        print("3.Exit")
        ch=input("enter a choice:")
        if ch=='1':
            admin_fun()
        elif ch=='2':
            pass
            # user_fun()
        elif ch=='3':
            break
        else:
            print("invalid choice ,try again")
def admin_fun():
    username=input("enter the name:")
    password=input("enter password:")
    if username in admin_credentials and admin_credentials[username] == password:
        while True:
            print("Admin Menu")
            print("1. Add Book")
            print("2. Update Book")
            print("3. Delete Book")
            print("4. Display All Books")
            print("5. Exit")
            ch= input("Select a choice: ")
            if ch =='1':
                add_book()
            elif ch=='2':
                update_book()
            elif ch=='3':
                delete_book()
            elif ch=='4':
                display()
            elif ch=='5':
                break
            else:
                print("Invalid option.")
    else:
        print("Invalid credentials")
def add_book():
    id = input("Enter book ID: ")
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    quantity = int(input("Enter book quantity: "))
    book[id] = {'title': title, 'author': author, 'quantity': quantity}
    print("Book added successfully.")
def update_book():
    id=input("enter  book id to update: ")
    if id in book:
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        quantity = int(input("Enter book quantity: "))
        book[id]={'title': title, 'author': author, 'quantity': quantity}
        print("Book updated ")
    else:
        print("no book found")
def delete_book():
    id=input("enter id you want to delete:")
    if id in book:
        del book[id]
        print("book deleted")
    else:
        print("book not found")
def display():
    
    for i in book:
     print(" ID:", book["id"])
print("Title:", book["title"])
print("Author:", book["author"])
print("Quantity:", book["quantity"])


# def user_fun():
#     user= []
#     while True:
#         print("User Menu")
#         print("1.Registration")
#         print("2.Login")
#         print("3.Exit")
#         ch= input("Select a choice: ")
#         if ch== '1':
#             register()
#         elif ch== '2':
#             if login():
#                 user_menu()
#         elif ch== '3':
#             break
#         else:
#             print("Invalid")
# def register():


main_menu()
