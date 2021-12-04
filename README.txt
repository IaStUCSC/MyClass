https://github.com/IaStUCSC/MyClass
This demo program creates a cash register for a school supplies store operating in the state of California. An object of a SuppliesCashRegister is created with its designation (Identification code), some money in the register, and a capacity for money (we assume only physical cash transactions are made). You can get and set these values (except the id, which can’t be edited after creation), as well as getting the items in the store’s inventory, handily preloaded onto the register! The main functionality, though, is start_transaction, which allows the user to input multiple purchases simply and efficiently, quickly updating the register. 

VARIABLES:
class variables:
__inventory holds a dictionary where the keys are the names of the items(all lower) and the values are their prices before taxes. (Some items may be only purchasable in bundles, those items’ names are plural).

__CA_sales_tax holds the info for California state sales tax as a float, which can be developer-side changed to easily edit all prices to match

data values:
__id is the register’s id (string), can only be interacted with by get_designation

__money_stored is the money within the register, stored as a float

__capacity is the total physical money the register can hold, stored as a float

METHODS:
helper function(s):
propose_deposit(proposal) handles an increase in money stored, checking if it would set it over capacity and rejecting it.

user functions:
get_designation() gets the id

get_money_stored() gets the money_stored

set_money_stored(new_val) sets the money_stored, unless that value is over capacity, in which case it sets it to full capacity

get_capacity() gets the capacity

set_capacity(new_val) sets the capacity, proper etiquette is to empty the register before changing the capacity.

unload_register() sets the money_stored back to 0

print_inventory() prints the item names in the inventory

get_price(item_name) returns the price of a item (after sales tax), given its name. returns “None” and prints an error message if no such item exists

purchase_item(item_name, quantity) buys quantity amount of items, updating money_stored to match

start_transaction() allows the user to input a command, from 5 options (entering an invalid command will raise a “item does not exist” error)
* “exit” ends the transaction
* “print inventory” calls the aforementioned print_inventory
* “$[cost]” directly inputs that amount of money
* “[item_name]” buys 1 of that item
* “[item_name], [quantity]” buys quantity amount of items

DEMO_PROGRAM:
The demo program is simple, it creates an instance of register (called myRegister), prints its inventory, shows the amount of money in it, and then runs a transaction. The user has the reference to the inventory (since it was just printed), and can purchase many items (as if they were the humble clerk to this fine register). Afterwards, it shows the user their new amount of money stored, and how close they are to capacity. 
To interact with the demo, simply input the commands (see start_transaction or read the printed message) to buy some nice school supplies, and then enter exit when you are done.

