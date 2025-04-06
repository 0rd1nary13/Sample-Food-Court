import time
import datetime
from person import Student, Staff
from burgers import Burger


class Order:
    def __init__(self):
        # "_" means they are private
        self._price_no_tax = 0
        self._price_after_tax = 0
        self._total_tax = 0
        self.name = "De Anza Food Court"

        self._menu_items = {
            "de_anza_burger": Burger("De Anza Burger", 1, 5.25),
            "bacon_cheese": Burger("Bacon Cheese", 2, 5.75), 
            "mushroom_swiss": Burger("Mushroom Swiss", 3, 5.95),
            "western_burger": Burger("Western Burger", 4, 5.95),
            "don_cali_burger": Burger("Don Cali Burger", 5, 5.95)
        }

        self._order_dict = {key: 0 for key in self._menu_items}

    # Delete the item from the order
    def delete_item(self):
        self.display_order()
        item_to_delete = input("Enter the index of the burger you'd like to delete: ").strip()
        try:
            item_index = int(item_to_delete) - 1
            if 0 <= item_index < len(self._order_dict):
                item_name = list(self._order_dict.keys())[item_index]
                del self._order_dict[item_name]  # Delete the item from the order dictionary
                print(f"{item_name} has been deleted from the order.")
            else:
                print("Please enter a valid menu item number.")
        except ValueError:
            print("Invalid input. Please enter a valid menu item number.")

    def display_order(self):
        print("Here is your current order")
        print("**********************************************************")
        for item_name, quantity in self._order_dict.items():
            if quantity > 0:
                print(f"{item_name} - Quantity: {quantity}")
        print("**********************************************************")

    def display_menu(self):
        print("            Welcome to", self.name)
        print("**********************************************************")
        menu_keys = list(self._menu_items.keys())
        for item_name, price in self._menu_items.items():
            print(f"{menu_keys.index(item_name) + 1:<5} {item_name:<30} ${price:>5.2f}")
        print("**********************************************************")

    def get_input(self):
        while True:
            print("Menu:")
            print("1. Order a burger")
            print("2. Delete an item from the order")
            print("3. Display current order")
            print("4. Display menu")
            print("5. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == '1':
                self.order_burger()
            elif choice == '2':
                self.delete_item()
            elif choice == '3':
                self.display_order()
            elif choice == '4':
                self.display_menu()
            elif choice == '5':
                print("Thank you, hope to see you again!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

    def order_burger(self):
        menu_keys = list(self._menu_items.keys())
        while True:
            try:
                print("Menu:")
                for index, item_name in enumerate(menu_keys, start=1):
                    print(f"{index}. {item_name} - ${self._menu_items[item_name]:.2f}")

                user_input = input("Enter the number of the burger you'd like to order, Enter 0 to go back: ").strip()
                if user_input == '0':
                    break

                item_index = int(user_input) - 1
                if 0 <= item_index < len(menu_keys):
                    item_name = menu_keys[item_index]
                    quantity = int(input(f"Enter the quantity for {item_name}: ").strip())
                    if quantity < 0:
                        raise ValueError("Quantity cannot be negative.")
                    self._order_dict[item_name] += quantity
                    print(f"{quantity} {item_name}(s) added to the order.")
                else:
                    print("Please enter a valid menu item number.")
            except ValueError as e:
                print(f"Invalid input: {e}")

    def calculate(self):
        customer_type = input("Is the customer a Student ? (y/n): ").strip().lower()
        if customer_type == 'y':
            self._price_no_tax = sum(self._order_dict[item] * self._menu_items[item] for item in self._order_dict)
            self._total_tax = self._price_no_tax * Student().get_tax_rate()
            self._price_after_tax = self._price_no_tax + self._total_tax
        else:
            self._price_no_tax = sum(self._order_dict[item] * self._menu_items[item] for item in self._order_dict)
            self._total_tax = self._price_no_tax * Staff().get_tax_rate()
            self._price_after_tax = self._price_no_tax + self._total_tax

    def print_bill(self):
        print("Here is your cost detail")
        print("**********************************************************")
        for item_name, quantity in self._order_dict.items():
            if quantity > 0:
                item_price = self._menu_items[item_name]
                item_cost = item_price * quantity
                print(f"{item_name} - Price: ${item_price}, Quantity: {quantity}, Cost: ${item_cost}")
        print("**********************************************************")
        print("The total before tax: ", round(self._price_no_tax, 2))
        print("Tax Amount: ", round(self._total_tax, 2))
        print("Total price after tax: ", round(self._price_after_tax, 2))

    def save_to_file(self):
        time_stamp = time.time()
        order_time_stamp = datetime.datetime.fromtimestamp(time_stamp).strftime('%Y-%m-%d %H-%M-%S')
        filename = order_time_stamp + '.txt'

        with open(filename, 'w') as file:
            file.write("            Here is your order detail:\n")
            file.write("**********************************************************\n")
            for item_name, quantity in self._order_dict.items():
                if quantity > 0:
                    item_price = self._menu_items[item_name]
                    item_cost = item_price * quantity
                    file.write(
                        f"{item_name} - Price: ${item_price:.2f}, Quantity: {quantity}, Cost: ${item_cost:.2f}\n")
            file.write("**********************************************************\n")
            file.write(f"Total before tax: ${self._price_no_tax:.2f}\n")
            file.write(f"Tax Amount: ${self._total_tax:.2f}\n")
            file.write(f"Total price after tax: ${self._price_after_tax:.2f}\n")
