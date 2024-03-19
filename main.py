# This program is a simple food ordering system for a food court. The user can order a burger, delete an item from
# the order, display the current order, display the menu, and exit the system. The program will calculate the total
# cost of the order and save the order to a file. The program will continue to take orders until the user decides to
# exit the system.
#Created by team Stack underflow on March 12 2024
#Di Zhang, Huiguang Ma

from Order import Order


def main():
    flag = True

    while flag:
        order = Order()
        order.display_menu()
        order.get_input()  # Note the correction to match the method name
        order.calculate()
        order.print_bill()
        order.save_to_file()

        user_input_to_continue = input("Continue for another order (Any key=Yes, n=No)? ").strip().lower()

        if user_input_to_continue == 'n':
            print("The system is shutting down!")
            flag = False


if __name__ == "__main__":
    main()


"""            Welcome to De Anza Food Court
**********************************************************
1     De Anza Burger                 $ 5.25
2     Bacon Cheese                   $ 5.75
3     Mushroom Swiss                 $ 5.95
4     Western Burger                 $ 5.95
5     Don Cali Burger                $ 5.95
**********************************************************
Menu:
1. Order a burger
2. Delete an item from the order
3. Display current order
4. Display menu
5. Exit
Enter your choice: 1
Menu:
1. De Anza Burger - $5.25
2. Bacon Cheese - $5.75
3. Mushroom Swiss - $5.95
4. Western Burger - $5.95
5. Don Cali Burger - $5.95
Enter the number of the burger you'd like to order, Enter 0 to go back: 2
Enter the quantity for Bacon Cheese: 3
3 Bacon Cheese(s) added to the order.
Menu:
1. De Anza Burger - $5.25
2. Bacon Cheese - $5.75
3. Mushroom Swiss - $5.95
4. Western Burger - $5.95
5. Don Cali Burger - $5.95
Enter the number of the burger you'd like to order, Enter 0 to go back: 4
Enter the quantity for Western Burger: 2
2 Western Burger(s) added to the order.
Menu:
1. De Anza Burger - $5.25
2. Bacon Cheese - $5.75
3. Mushroom Swiss - $5.95
4. Western Burger - $5.95
5. Don Cali Burger - $5.95
Enter the number of the burger you'd like to order, Enter 0 to go back: 0
Menu:
1. Order a burger
2. Delete an item from the order
3. Display current order
4. Display menu
5. Exit
Enter your choice: 3
Here is your current order
**********************************************************
Bacon Cheese - Quantity: 3
Western Burger - Quantity: 2
**********************************************************
Menu:
1. Order a burger
2. Delete an item from the order
3. Display current order
4. Display menu
5. Exit
Enter your choice: 2
Here is your current order
**********************************************************
Bacon Cheese - Quantity: 3
Western Burger - Quantity: 2
**********************************************************
Enter the index of the burger you'd like to delete: 2
Bacon Cheese has been deleted from the order.
Menu:
1. Order a burger
2. Delete an item from the order
3. Display current order
4. Display menu
5. Exit
Enter your choice: 3
Here is your current order
**********************************************************
Western Burger - Quantity: 2
**********************************************************
Menu:
1. Order a burger
2. Delete an item from the order
3. Display current order
4. Display menu
5. Exit
Enter your choice: 5
Thank you, hope to see you again!
Is the customer a Student ? (y/n): y
Here is your cost detail
**********************************************************
Western Burger - Price: $5.95, Quantity: 2, Cost: $11.9
**********************************************************
The total before tax:  11.9
Tax Amount:  0.0
Total price after tax:  11.9
Continue for another order (Any key=Yes, n=No)? y
            Welcome to De Anza Food Court
**********************************************************
1     De Anza Burger                 $ 5.25
2     Bacon Cheese                   $ 5.75
3     Mushroom Swiss                 $ 5.95
4     Western Burger                 $ 5.95
5     Don Cali Burger                $ 5.95
**********************************************************
Menu:
1. Order a burger
2. Delete an item from the order
3. Display current order
4. Display menu
5. Exit
Enter your choice: 1
Menu:
1. De Anza Burger - $5.25
2. Bacon Cheese - $5.75
3. Mushroom Swiss - $5.95
4. Western Burger - $5.95
5. Don Cali Burger - $5.95
Enter the number of the burger you'd like to order, Enter 0 to go back: 2
Enter the quantity for Bacon Cheese: 3
3 Bacon Cheese(s) added to the order.
Menu:
1. De Anza Burger - $5.25
2. Bacon Cheese - $5.75
3. Mushroom Swiss - $5.95
4. Western Burger - $5.95
5. Don Cali Burger - $5.95
Enter the number of the burger you'd like to order, Enter 0 to go back: 4
Enter the quantity for Western Burger: 23
23 Western Burger(s) added to the order.
Menu:
1. De Anza Burger - $5.25
2. Bacon Cheese - $5.75
3. Mushroom Swiss - $5.95
4. Western Burger - $5.95
5. Don Cali Burger - $5.95
Enter the number of the burger you'd like to order, Enter 0 to go back: 23
Please enter a valid menu item number.
Menu:
1. De Anza Burger - $5.25
2. Bacon Cheese - $5.75
3. Mushroom Swiss - $5.95
4. Western Burger - $5.95
5. Don Cali Burger - $5.95
Enter the number of the burger you'd like to order, Enter 0 to go back: 23
Please enter a valid menu item number.
Menu:
1. De Anza Burger - $5.25
2. Bacon Cheese - $5.75
3. Mushroom Swiss - $5.95
4. Western Burger - $5.95
5. Don Cali Burger - $5.95
Enter the number of the burger you'd like to order, Enter 0 to go back: 2
Enter the quantity for Bacon Cheese: 1
1 Bacon Cheese(s) added to the order.
Menu:
1. De Anza Burger - $5.25
2. Bacon Cheese - $5.75
3. Mushroom Swiss - $5.95
4. Western Burger - $5.95
5. Don Cali Burger - $5.95
Enter the number of the burger you'd like to order, Enter 0 to go back: 2
Enter the quantity for Bacon Cheese: 3
3 Bacon Cheese(s) added to the order.
Menu:
1. De Anza Burger - $5.25
2. Bacon Cheese - $5.75
3. Mushroom Swiss - $5.95
4. Western Burger - $5.95
5. Don Cali Burger - $5.95
Enter the number of the burger you'd like to order, Enter 0 to go back: 0
Menu:
1. Order a burger
2. Delete an item from the order
3. Display current order
4. Display menu
5. Exit
Enter your choice: 5
Thank you, hope to see you again!
Is the customer a Student ? (y/n): y
Here is your cost detail
**********************************************************
Bacon Cheese - Price: $5.75, Quantity: 7, Cost: $40.25
Western Burger - Price: $5.95, Quantity: 23, Cost: $136.85
**********************************************************
The total before tax:  177.1
Tax Amount:  0.0
Total price after tax:  177.1
Continue for another order (Any key=Yes, n=No)? n
The system is shutting down!

Process finished with exit code 0
"""
