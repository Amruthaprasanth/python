admin_credentials =["amrutha", "1234"]
products =[]
orders =[]

def menu():
    while True:
        print("Online Shopping")
        print("1. Admin")
        print("2. User")
        print("3. Exit")
        ch = input("Enter your choice: ")
        if ch == '1':
            admin()
        elif ch == '2':
            user()
        elif ch == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

def admin():
    username = input("Enter username: ")
    password = input("Enter password: ")
    for i in admin_credentials:
        if i[0]==username and i[1]==password:
            admin()
    else:
        print("Invalid credentials")

def admin():
    while True:
        print("Admin Menu")
        print("1.Add Product")
        print("2.Update Product")
        print("3.Remove Product")
        print("4.View All Products")
        print("5.View Orders")
        print("6.Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_product()
        elif choice == "2":
            update_product()
        elif choice == "3":
            remove_product()
        elif choice == "4":
            view_all_products()
        elif choice == "5":
            view_orders()
        elif choice == "6":
            return
        else:
            print("Invalid choice")

def add_product():
    product_id = input("Enter product id: ")
    name = input("Enter product name: ")
    description = input(" product description: ")
    price = float(input("Enter product price: "))  # Assuming valid input
    products.append([product_id, name, description, price])
    print("Product added")

def update_product():
    product_id = input("Enter product ID to update: ")
    found =False  
    for product in products:
        if product[0] == product_id:
            product[1] = input("Enter new product name: ")
            product[2] = input("Enter new product description: ")
            product[3] = float(input("Enter new product price: "))
            print("Product updated successfully.")
            found = True  
            break  
    if not found:
        print("Product not found.") 
def remove_product():
    product_id = input("Enter product ID to remove: ")
    for product in products:
        if product[0] == product_id:
            products.remove(product)
            print("Product removed successfully.")
            break
        else:
            print("Product not found.")

def view_all_products():
    if not products:
        print("No products available.")
    else:
        for product in products:
            print("ID: {}, Name: {}, Description: {}, Price: ${:.2f}".format(product[0], product[1], product[2], product[3]))

def user():
    while True:
        print("\nUser Menu")
        print("1. View Products")
        print("2. Place Order")
        print("3. View Orders")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            view_all_products()
        elif choice == '2':
            place_order()
        elif choice == '3':
            view_orders()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

def place_order():
    order_id = input("Enter Order id: ")
    product_id = input("Enter Product id to order: ")
    found=False
    for product in products:
        if product[0] ==product_id:
            orders.append([order_id, product_id, product[1], product[3], "Pending"])
            print("Ordered")
            found=True
            break
    if found==False:
        print("Product not found")

def view_orders():
    if len(orders) ==0:
        print("No orders")
    else:
        print("Orders")
        for order in orders:
            print("Order id: {}, Product ID: {}, Product Name: {}, Price: ${:.2f}, Status:  {}".format(order[0], order[1], order[2], order[3], order[4]))

menu()