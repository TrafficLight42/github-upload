#Customer Class:
class customer:
    global stock
    def __init__(self):
        self.basket = []

    def add_item(self, item):
        if str(item) in stock:        
            self.basket.append(str(item))
            print("\033[92m", "\n", item, " added to basket.", "\033[0m")
        else:
            print("\033[91m", "\nItem not in stock.", "\033[0m")

    def remove_item(self, item):
        try:
            self.basket.remove(str(item))
            print("\033[92m", "\n", item, " removed from basket.", "\033[0m")
        except:
            print("\033[91m", "\n Item not in basket.", "\033[0m")

    def print_basket(self):
        print("\033[92m", "\nThe Customer's basket: ", self.basket, "\033[0m")

    def get_basket(self):
        return self.basket

stock = {
        "Apple": 2.99,
        "Cheese": 3.99,
        "Pencil": 0.99,
        "Carrott": 2.50
        }

def mainMenu():
    global customer1
    print("\n---------- Main Menu ----------")
    print("\nAdd an item to the customer's basket: a",
            "\nRemove an item from the customer's basket: r",
            "\nShow the customer's basket: b",
            "\nPrint the customer's receipt: p")
    option = input("Select an option: ")

    if option == "n":
        customer1 = customer()
        print("New customer created")

    elif option == "a":
        item = input("Enter the item to be added: ")
        customer1.add_item(item)

    elif option == "r":
        item = input("Enter the item to be removed: ")
        customer1.remove_item(item)

    elif option == "b":
        customer1.print_basket()

    elif option == "p":
        for x in range (0, 5):
            print("")

        print("---------- Receipt ----------")
        print("\nItems:")

        basket = customer1.get_basket()
        total = 0
        for x in range (0, len(basket)):
            print(basket[x], stock[basket[x]])
            total += stock[basket[x]]

        print("\nTotal Price: ", str(total))

        wait = input("\n\n\nPress Enter to return to the main menu...")
        customer1 = customer()

    elif option == "exit":
        exit()

    else:
        print("\033[91m", "Invalid Option!", "\033[0m")

#Testing
customer1 = customer()
while True:
    mainMenu()
