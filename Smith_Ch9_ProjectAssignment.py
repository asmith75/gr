#part one!

class ItemToPurchase:
    def __init__(self,item_name,item_price,item_quantity):
        self.item_name = str(item_name)
        self.item_price = float(item_price)
        self.item_quantity = int(item_quantity)

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        return f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}"

def create_item():
    item_name = input("Enter item name: ")
    item_price = input("Enter item price: ")
    item_quantity = input("Enter item quantity: ")

    item = ItemToPurchase(item_name, item_price, item_quantity)
    print(item.print_item_cost())
    return item 

#part two!!
def create_two_items():
    print("Item 1")
    item1 = create_item()
    print("\nItem 2")
    item2 = create_item()
    
    return item1, item2 

#part threee!
def show_total_cost(item1,item2):
    total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
    print("\nTOTAL COST")
    print(item1.print_item_cost())
    print(item2.print_item_cost())
    print(f"Total: ${total_cost:.2f}")

def main():
    item1, item2 = create_two_items()
    show_total_cost(item1, item2)

main()

