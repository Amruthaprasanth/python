
class Library:
    def __init__(self):
        self.books=[]
        self.admin_details={'admin':'123'}
        self.users=[]

    def menu(self):
        while True:
            print("Main Menu:")
            print("1. Admin")
            print("2. User")
            print("3. Exit")
            ch = input("Select an option: ")
            if ch == '1':
                self.admin()
            elif ch == '2':
                self.user()
            elif ch == '3':
                print("Exit")
                break
            else:
                print("Invalid choice")

    def admin(self):
        username = input("Enter admin username: ")
        password = input("Enter admin password: ")
        if username in self.admin_details and self.admin_details[username] == password:
            while True:
                print("Admin Menu:")
                print("1. Add Book")
                print("2. Update Book")
                print("3. Delete Book")
                print("4. Display All Books")
                print("5. Exit")
                choice = input("Select an option: ")
                if choice=='1':
                    self.add()
                elif choice=='2':
                    self.update()
                elif choice=='3':
                    self.delete()
                elif choice== '4':
                    self.display()
                elif choice=='5':
                    break
                else:
                    print("Invalid choice")

    def add(self):
        book_id = input("Enter Book ID: ")
        title = input("Enter book name: ")
        author = input("Enter Author: ")
        quantity = int(input("Enter Quantity: "))
        new_book = {'book_id': book_id, 'title': title, 'author': author, 'quantity': quantity}
        self.books.append(new_book)
        print("Book added successfully.")

    def update(self):
        book_id = input("Enter Book id to update: ")
        book = None
        for b in self.books:
            if b['book_id'] == book_id:
                book = b
                break
        if book is None:
            print("Book id not found.")
            return
        print(f"Current details: ID: {book['book_id']}, Title: {book['title']}, Author: {book['author']}, Quantity: {book['quantity']}")
        title = input("Enter new Title: ")
        author = input("Enter new Author: ")
        quantity_input = input("Enter new Quantity: ")
        if title:
            book['title'] = title
        if author:
            book['author'] = author
        if quantity_input:
            book['quantity'] = int(quantity_input)
        print("Book updated successfully.")

    def delete(self):
        book_id = input("Enter Book ID to delete: ")
        for b in self.books:
            if b['book_id'] == book_id:
                self.books.remove(b)
                print("Book deleted successfully.")
                return
        print("Book ID not found.")

    def display(self):
        if not self.books:
            print("No books available.")
        else:
            for book in self.books:
                print(f"ID: {book['book_id']}, Title: {book['title']}, Author: {book['author']}, Quantity: {book['quantity']}")

    def user(self):
        while True:
            print("User Menu:")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Select an option: ")
            if choice == '1':
                self.register()
            elif choice == '2':
                self.login()
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")

    def register(self):
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        address = input("Enter Address: ")
        phone_number = input("Enter Phone Number: ")
        for user in self.users:
            if user[3] == phone_number:
                print("Phone number already exists.")
                return
        username = input("Enter username: ")
        for user in self.users:
            if user[4] == username:
                print("Username already used.")
                return
        password = input("Enter Password: ")
        user = [name, age, address, phone_number, username, password]
        self.users.append(user)
        print("Registration successful.")

    def login(self):
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        for user in self.users:
            if user[4] == username and user[5] == password:
                print("Login successful!")
                return
        print("Invalid username or password.")

    def user(self):
        while True:
            print("User Menu:")
            print("1. Display All Books")
            print("2. Search Book by Name")
            print("3. Exit")
            choice = input("Select an option: ")
            if choice == '1':
                self.display()
            elif choice == '2':
                self.search()
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")

    def search(self):
        title = input("Enter the title of the book to search: ")
        found = False
        for book in self.books:
            if book['title'] == title:
                print(f"Found: ID: {book['book_id']}, Title: {book['title']}, Author: {book['author']}, Quantity: {book['quantity']}")
                found = True
                break
        if not found:
            print("Book not found.")

library = Library()
library.menu()