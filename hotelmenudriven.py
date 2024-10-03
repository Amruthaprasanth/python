admin_credentials = {'admin': '1234'}
rooms = {}
receptionist_credentials = {'receptionist': '456'}
reservations = []
guests = []
current_guest_id = 1

def main_menu():
    while True:
        print("HOTEL RESERVATION SYSTEM")
        print("1. Admin")
        print("2. Receptionist")
        print("3. Guest")
        choice = input("Enter your choice: ")
        if choice == '1':
            admin()
        elif choice == '2':
            receptionist()
        elif choice == '3':
            guest()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

def admin():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in admin_credentials and admin_credentials[username] == password:
        while True:
            print("Admin Menu")
            print("1. Add Room")
            print("2. Update Room Details")
            print("3. Remove Room")
            print("4. View All Reservations")
            print("5. Generate Reports")
            print("6. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                add_room()
            elif choice == '2':
                update_room()
            elif choice == '3':
                remove_room()
            elif choice == '4':
                view_reservations()
            elif choice == '5':
                generate_reports()
            elif choice == '6':
                print("Exiting...")
                break
            else:
                print("Invalid choice.")
    else:
        print("Incorrect username or password.")

def add_room():
    number = input("Enter room number: ")
    room_type = input("Enter room type: ")
    price = float(input("Enter price per night: "))
    rooms[number] = {'type': room_type, 'price': price, 'available': 'yes'}
    print("Room added successfully.")

def update_room():
    number = input("Enter the room number to update: ")
    if number in rooms:
        room_type = input("Enter new room type: ")
        price = float(input("Enter new price: "))
        rooms[number] = {'type': room_type, 'price': price, 'available': rooms[number]['available']}
        print("Room updated successfully.")
    else:
        print("Room not found.")

def remove_room():
    number = input("Enter room number to remove: ")
    if number in rooms:
        del rooms[number]
        print("Room removed successfully.")
    else:
        print("Room not found.")

def view_reservations():
    print("Reservations:")
    if not reservations:
        print("No reservations found.")
    else:
        for reservation in reservations:
            print(reservation)

def generate_reports():
    total_rooms = len(rooms)
    available_rooms = 0
    occupied_rooms = 0
    for room in rooms.values():
        if room['available'] == 'yes':
            available_rooms += 1
        else:
            occupied_rooms += 1
    print(f"Total Rooms: {total_rooms}")
    print(f"Available Rooms: {available_rooms}")
    print(f"Occupied Rooms: {occupied_rooms}")

def receptionist():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in receptionist_credentials and receptionist_credentials[username] == password:
        while True:
            print("Receptionist Menu")
            print("1. Check-In Guest")
            print("2. Check-Out Guest")
            print("3. Make Reservation")
            print("4. Cancel Reservation")
            print("5. View Available Rooms")
            print("6. View Guest Details")
            print("7. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                check_in()
            elif choice == '2':
                check_out()
            elif choice == '3':
                make_reservation()
            elif choice == '4':
                cancel_reservation()
            elif choice == '5':
                view_available_rooms()
            elif choice == '6':
                view_guest_details()
            elif choice == '7':
                print("Exiting...")
                break
            else:
                print("Invalid choice.")
    else:
        print("Incorrect username or password.")

def check_in():
    guest_id = input("Enter guest ID: ")
    room_number = input("Enter room number: ")
    check_in_date = input("Enter check-in date: ")
    if room_number in rooms and rooms[room_number]['available'] == 'yes':
        rooms[room_number]['available'] = 'no'
        guest_name = input("Enter guest name: ")
        guests.append([guest_id, guest_name, room_number, check_in_date])
        print("Guest checked in successfully.")
    else:
        print("Room is not available.")

def check_out():
    guest_id = input("Enter guest ID: ")
    room_number = None
    for guest in guests:
        if guest[0] == guest_id:
            room_number = guest[2]
            break
    if room_number is not None:
        rooms[room_number]['available'] = 'yes'
        guests[:] = [guest for guest in guests if guest[0] != guest_id]
        print("Guest checked out successfully.")
    else:
        print("Guest not found.")

def make_reservation():
    guest_id = input("Enter guest ID: ")
    room_number = input("Enter room number: ")
    check_in_date = input("Enter check-in date: ")
    check_out_date = input("Enter check-out date: ")
    if room_number in rooms and rooms[room_number]['available'] == 'yes':
        rooms[room_number]['available'] = 'reserved'
        reservations.append([guest_id, room_number, check_in_date, check_out_date])
        print("Room reserved successfully.")
    else:
        print("Room not available for reservation.")

def cancel_reservation():
    guest_id = input("Enter guest ID to cancel reservation: ")
    for reservation in reservations:
        if reservation[0] == guest_id:
            reservations.remove(reservation)
            room_number = reservation[1]
            rooms[room_number]['available'] = 'yes'
            print("Reservation canceled successfully.")
            return
    print("No reservation found.")

def view_available_rooms():
    available_rooms = [number for number in rooms if rooms[number]['available'] == 'yes']
    if available_rooms:
        for number in available_rooms:
            print(f"Room Number: {number}, Type: {rooms[number]['type']}, Price: {rooms[number]['price']}")
    else:
        print("No available rooms.")

def view_guest_details():
    guest_id = input("Enter guest ID: ")
    for guest in guests:
        if guest[0] == guest_id:
            print("Guest Details:")
            print("Name:", guest[1])
            print("Room Number:", guest[2])
            print("Check-In Date:", guest[3])
            return
    print("Guest not found.")

def guest():
    while True:
        print("Guest Menu")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

def register():
    global current_guest_id
    name = input("Enter name: ")
    contact = input("Enter contact details: ")
    address = input("Enter address: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    guest_id = current_guest_id
    current_guest_id += 1
    guests.append([guest_id,name, contact, address, username, password])
    print("Registration successful.")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    for guest in guests:
        if guest[3] == username and guest[4] == password:
            print("Login successful.")
            guest_menu(guest)
            return
    print("Username or password incorrect.")

def guest_menu(guest):
    while True:
        print("Guest Menu")
        print("1. View Available Rooms")
        print("2. Make a Reservation")
        print("3. View Reservation Status")
        print("4. Update Personal Information")
        print("5. Cancel Reservation")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            view_available_rooms()
        elif choice == '2':
            make_reservation()
        elif choice == '3':
            view_reservation_status(guest)
        elif choice == '4':
            update_personal_info(guest)
        elif choice == '5':
            cancel_reservation()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

def view_reservation_status(guest):
    guest_id = guest[0]
    for reservation in reservations:
        if reservation[0] == guest_id:
            print("Current Reservation Status:")
            print("Room Number:", reservation[1])
            print("Check-In Date:", reservation[2])
            print("Check-Out Date:", reservation[3])
            return
    print("No reservation found.")

def update_personal_info(guest):
    new_contact = input("Enter new contact details: ")
    new_address = input("Enter new address: ")
    guest[1] = new_contact
    guest[2] = new_address
    print("Personal information updated successfully.")

main_menu()