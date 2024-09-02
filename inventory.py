import sys
class inventory():
    def __init__(self):
        self.inventory = []
    def __add_product__(self, name, price, quantity, category, threshold, amount_sold):
        self.inventory.append({'name':name, 'quantity':quantity, 'price':price, 
                               'categories':category, 'threshold': threshold, 
                               'amount_sold': amount_sold})
    def __remove_product__(self, name):
        for i in self.inventory:
            if i['name'] == name:
                self.inventory.remove(i)
            else:
                print('item not found')
    def __update_product__(self,name, quantity, amount_sold = None):
        for i in self.inventory:
            if i['name'] == name:
                i['quantity'] = quantity
                if amount_sold != None:
                    i['amount_sold'] += amount_sold
                if quantity < i['threshold']:
                    print("This item has gone below the threshold")
            else:
                print('item not found')
    def __display__(self):
        print(self,inventory)
    def __search__(self, name):
        for i in self.inventory:
            if i['name'] == name:
                return(i)
            else:
                print('item not found')
    def __display_sales_table(self):
        list_ = []
        revenue = 0
        for i in self.inventory:
            list_.append({'name':i['name'], 'quantity_sold':i['amount_sold']})
            revenue += i['amount_sold']*i['price']
        print(list_)
        print('Total Revenue Generated is: {}'.format(revenue))
    def __quit__(self):
        quit
a = input('Type start to create an inventory or any other key to exit: ')
if a == 'start':
    inventory = inventory()
    while True:
        action = input("1. Add a product\n2.Remove a product\n3. Update a product's quantity\n4. Display full inventory\n5. Search for an item by name\n6. Display all sales\n7. quit\n")
        if action == 1:
            name = input('name: ')
            price = input('price: ')
            quantity = input('quantity: ')
            category = input('category: ')
            threshold = input('threshold: ')
            amount = input('amount sold: ')
            inventory.add_product( name, price, quantity, category, threshold, amount)
            print('product added')
        elif action == 2:
            name = input('name of product to be removed: ')
            inventory.remove_product(name)
        elif action == 3:
            name = input('name of product to be removed: ')
            quantity = input('new quantity: ')
            amount = input('amount of product sold(if none type 0): ')
            inventory.update_product(name, quantity, amount)
        elif action == 4:
            inventory.display()
        elif action == 5:
            name = input("name of product you're looking for: ")
            inventory.search(name)
        elif action == 6:
            inventory.display_sales_table()
        elif action == 7:
            sys.exit()
else:
    sys.exit()
    