class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.balance = 0
        self.past_orders = []

    def view_menu(self, restaurent):
        restaurent.view_menu()

    def view_balance(self):
        print(f"Your balance is: ${self.balance}")
        
    def add_balance(self, amount):
        self.balance += amount
        print(f"\n${amount} added successfully! Your new balance is: ${self.balance}")
    
    def place_order(self, restaurent, item_name, quantity):
        item_availablity = [item for item in restaurent.menu if item[0].lower() == item_name.lower()]
        if(item_availablity):
            total_price = item_availablity[0][1] * quantity
            if(self.balance >= total_price):
                self.balance -= total_price
                print(f"\nItem Name: {item_availablity[0][0].lower()}\nTotal Price: {total_price}\nOrder placed successfully!\nYour new balance is: ${self.balance}")
                self.past_orders.append((item_name, quantity, total_price))
            else:
                print("\nInsufficient balance!")
        else:
            print("\nItem not found!")

    def view_past_orders(self):
        if(len(self.past_orders)>0):
            print(f"\n--- Past Orders: {len(self.past_orders)} ---\nItem\t\tQuantity\tTotal Price")
            for order in self.past_orders:
                print(f"{order[0].lower()}\t\t{order[1]}\t\t{order[2]}")
        else:
            print("\nNo orders available!")


class Admin:
    def __init__(self, name):
        self.name = name

    def add_customer(self, restaurant, name, email, address):
        ct = Customer(name, email, address)
        restaurant.customers.append(ct)
        print(f"\nCustomer {name} added successfully!")

    def remove_customer(self, restaurant, name):
        restaurant.delete_customer(restaurant, name)

    def view_customers(self, restaurant):
        restaurant.customers_details(restaurant)
    
    def manage_restaurent_addItem(self, restaurent, item_name, price):
        restaurent.add_item(item_name, price)

    def manage_restaurent_removeItem(self, restaurent,item_name):
        restaurent.remove_item(item_name)

    def manage_restaurent_updatePrice(self, restaurent, item_name, new_price):
        restaurent.update_price(item_name, new_price)
    
class Restaurant:
    customers = []
    admins = []
    def __init__(self, name):
        self.name = name
        self.menu = []

    def add_item(self, item_name, price):
        self.menu.append((item_name, price))
        print(f"\n{item_name.lower()} added successfully!")

    def remove_item(self, item_name):
        item_availablity = [item for item in self.menu if item[0].lower() == item_name.lower()]
        if(item_availablity):
            self.menu.remove(item_availablity[0])
            print(f"\n{item_name.lower()} removed successfully!")
        else:
            print("\nItem not found!")

    def update_price(self, item_name, new_price):
        item_availablity = [item for item in self.menu if item[0].lower() == item_name.lower()]
        if(item_availablity):
            self.menu.remove(item_availablity[0])
            self.menu.append((item_name, new_price))
            print(f"\n{item_name.lower()} price updated successfully!")
        else:
            print("\nItem not found!")

    def customers_details(self, restaurant):
        if(len(restaurant.customers)>0):
            print(f"\n--- Customers: {len(restaurant.customers)} ---\nName\tEmail\t\tAddress")
            for ct in restaurant.customers:
                print(f"{ct.name}\t{ct.email}\t{ct.address}")
        else:
            print("No customers available!")

    def delete_customer(self, restaurant, name):
        ct_availablity = [ct for ct in restaurant.customers if ct.name.lower() == name.lower()]
        if(ct_availablity):
            restaurant.customers.remove(ct_availablity[0])
            print("\nCustomer removed successfully!")
        else:
            print("\nCustomer not found!")

    def view_menu(self):
        if(len(self.menu)>0):
            print(f"\n--- Menu Items: {len(self.menu)} ---")
            for item in self.menu:
                print(f"{item[0]}:\t${item[1]}")
        else:
            print("\nNo items available!")

res = Restaurant("Ma'er Hotel")
while True:
    print(f"\n--- {res.name} Management System ---")
    print("1. Admin\n2. Customer\n3. Exit")
    choice = input("Enter an option: ")
    if(choice == "1"):
        admin_name = input("Enter your name: ")
        check_admin = [admin for admin in Restaurant.admins if admin.name.lower() == admin_name.lower()]
        if(check_admin):
            ad = check_admin[0]
        else:
            ad = Admin(admin_name)
            Restaurant.admins.append(ad)
        while True:
            print(f"\nWelcome Admin: {admin_name}")
            print("\n--- Admin Menu ---")
            print("1. Add Customer\n2. Remove Customer\n3. View All Customers\n4. Manage Restaurant\n5. Exit")
            choice = input("Enter an option: ")
            if(choice == "1"):
                name = input("Enter name: ")
                email = input("Enter email: ")
                address = input("Enter address: ")
                ad.add_customer(res, name, email, address)
            elif(choice == "2"):
                name = input("Enter customer name: ")
                ad.remove_customer(res, name)
            elif(choice == "3"):
                ad.view_customers(res)
            elif(choice == "4"):
                while True:
                    print("\n--- Restaurant Management Menu ---")
                    print("1. Add Item\n2. Remove Item\n3. Update Price\n4. View Menu\n5. Exit")
                    choice = input("Enter an option: ")
                    if(choice == "1"):
                        item_name = input("Enter item name: ")
                        price = float(input("Enter price: "))
                        ad.manage_restaurent_addItem(res, item_name, price)
                    elif(choice == "2"):
                        item_name = input("Enter item name: ")
                        ad.manage_restaurent_removeItem(res, item_name)
                    elif(choice == "3"):
                        item_name = input("Enter item name: ")
                        new_price = float(input("Enter new price: "))
                        ad.manage_restaurent_updatePrice(res, item_name, new_price)
                    elif(choice == "4"):
                        res.view_menu()
                    elif(choice == "5"):
                        break
                    else:
                        print("Invalid choice!")
            elif(choice == "5"):
                break
            else:
                print("Invalid choice!")
    elif(choice == "2"):
        customer_name = input("Enter Customer Username: ")
        customer_availabiliy=[customer for customer in res.customers if customer.name == customer_name]
        if(customer_availabiliy):
            ct = customer_availabiliy[0]
            while True:
                print(f"\n--- {ct.name}'s Menu ---")
                print("1. View Restaurant Menu\n2. View Balance\n3. Add Balance\n4. Place Order\n5. View Past Orders\n6. Exit")
                choice = input("Enter an option: ")
                if(choice == "1"):
                    ct.view_menu(res)
                elif(choice == "2"):
                    ct.view_balance()
                elif(choice == "3"):
                    amount = float(input("Enter amount: "))
                    ct.add_balance(amount)
                elif(choice == "4"):
                    item_name = input("Enter item name: ")
                    quantity = int(input("Enter quantity: "))
                    ct.place_order(res, item_name, quantity)
                elif(choice == "5"):
                    ct.view_past_orders()
                elif(choice == "6"):
                    break
                else:
                    print("Invalid choice!")
        else:
            print("\nCustomer not found!")
    elif(choice == "3"):
        print("Exiting Restaurant Management System...")
        break
    else:
        print("Invalid choice!")