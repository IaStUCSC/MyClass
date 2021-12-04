# Ian S
# Python 3.8.2
# My Class
# The goal of this assignment is to practice making classes by creating a custom class
# Read README for more info

# I choose to model a cash register, this one is for a school supplies store in California
class SuppliesCashRegister:
    # Item Inventory with preset items and prices
    __inventory = {"glue sticks" : 2.49, "white out" : 1.79, "folder" : 1.49, 
    "glue" : 2.09, "pencil pack" : 2.79, "crayons" : 1.34, "binder" : 5.29, 
    "sharpies" : 13.29, "bic pens" : 7.49, "backpack" : 34.99,
    "markers" : 4.49, "white out" : 17.99, "notebook" : 2.03,
    "gel pens" : 18.29, "ti-84+ ce" : 154.99, "post-its" : 8.49,
    "index cards" : 1.99, "colored pencils" : 4.49}
    __CA_sales_tax = 0.0725

    # initializer sets the name, as well as money stored and capacity values.
    def __init__(self, designation, starting_money = 0, capacity = 3600):
        self.__id = designation
        if (starting_money > capacity):
            self.__money_stored = capacity
        else:
            self.__money_stored = starting_money
        self.__capacity = capacity

    # helper function for any time a purchase is made
    def propose_deposit(self, proposed_deposit):
        if (self.__money_stored == self.__capacity):
            print("register full, unload register first")
        elif(self.__money_stored + proposed_deposit > self.__capacity):
            print(f"you attempted to deposit {proposed_deposit:.2f}, whcih would overflow capacity by {self.__money_stored + proposed_deposit - self.__capacity}.\nPlease unload register first")
        else:
            self.__money_stored += proposed_deposit

    # returns the id
    def get_designation(self):
        return self.__id
    
    # no function for set_id, I want it to be constant after creation

    # getters and setters for basic inventory
    def get_money_stored(self):
        return self.__money_stored

    # setting money over capacity simply floors itself at capacity
    def set_money_stored(self, new_money):
        if (new_money > self.__capacity):
            self.__money_stored = self.__capacity
        else:
            self.__money_stored = new_money

    def get_capacity(self):
        return self.__capacity

    def set_capacity(self, new_capacity):
        self.__capacity = new_capacity
        if (new_capacity < self.__money_stored):
            print("money over new capacity was voided")
            self.set_money_stored(new_capacity)

    # unloads register (quick function)
    def unload_register(self):
        self.set_money_stored(0)
    
    #prints the items available for purchase (for the person working the register's convenience)
    def print_inventory(self):
        print(list(self.__inventory.keys()))

    def get_price(self, item_name):
        item_name_lower = item_name.lower()
        try:
            # get taxed by the state of california, fool
            cost = round(self.__inventory[item_name_lower] * (self.__CA_sales_tax + 1), 2)
            return cost
        except KeyError:
            print(f"error: item {item_name} not in inventory")
            return None

    # purchase one type of item
    def purchase_item(self, item_name, quantity):
        cost = self.get_price(item_name) * quantity
        self.propose_deposit(cost)

    # starts a transaction, which allows the user to input many items
    def start_transaction(self):
        print("enter format 'exit', 'print inventory', $[cost], [ItemName] to buy 1 of item, or [ItemName, Quantity]")
        while(True):
            command = input(">>> ")
            if (command == "exit"):
                print("transaction ended")
                break
            elif (command == "print inventory"):
                self.print_inventory()
            elif (command[0] == '$'):
                cost = float(command[1:])
                self.propose_deposit(cost)
                print("purchase confirmed")
            elif (command.find(", ") == -1):
                check = self.get_price(command)
                if (check != None):
                    self.purchase_item(command, 1)
                    print("purchase confirmed")
                else:
                    continue
            else:
                spliced = command.split(", ")
                item = spliced[0]
                quantity = float(spliced[1])
                check = self.get_price(item)
                if (check != None):
                    self.purchase_item(item, quantity)
                    print("purchase confirmed")
                else:
                    continue

def main():
    # create new register
    myRegister = SuppliesCashRegister("A12022021")
    # see the inventory
    print("The items are: ")
    myRegister.print_inventory()
    print(f"Your current amount of money stored is {myRegister.get_money_stored()}")
    # runs the transaction protocol (see README for more info)
    print("begin transaction:")
    myRegister.start_transaction()
    # shows money 
    print(f"Register {myRegister.get_designation()} now has: ${myRegister.get_money_stored()}")
    print(f"Capacity of register is ${myRegister.get_capacity()}, currently ${myRegister.get_capacity() - myRegister.get_money_stored()} under capacity")

if __name__ == "__main__":
    main()

