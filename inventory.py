import sys
inventory = []
def add_product(name, price, quantity, category, threshold, amount_sold):
    inventory.append({'name':name, 'quantity':quantity, 'price':price, 
                           'categories':category, 'threshold': threshold, 
                           'amount_sold': amount_sold})
def remove_product(name):
    for i in inventory:
        if i['name'] == name:
            inventory.remove(i)
            print('ITEM REMOVED\n')
        else:
            print('item not found\n')
def update_product(name, quantity, amount_sold = None):
    for i in inventory:
        if i['name'] == name:
            i['quantity'] = quantity
            if amount_sold != None:
                i['amount_sold'] += amount_sold
            if int(quantity) < int(i['threshold']):
                print("This item has gone below the threshold\n")
        else:
            print('item not found\n')
def display():
    print(inventory)
    print('\n')
def search(name):
    for i in inventory:
        if i['name'] == name:
            print(i)
            print('\n')
        else:
            print('item not found\n')
def display_sales_table():
    list_ = []
    revenue = 0
    for i in inventory:
        list_.append({'name':i['name'], 'quantity_sold':i['amount_sold']})
        revenue += int(i['amount_sold'])*int(i['price'])
    print(list_)
    print('Total Revenue Generated is: {}\n'.format(revenue))

a = input('Type start to create an inventory or any other key to exit: ')
if a == 'start':
    while True:
        action = input("\nType any of the following numbers to perform the associated operations:\n1. Add a product\n2. Remove a product\n3. Update a product's quantity\n4. Display full inventory\n5. Search for an item by name\n6. Display all sales\n7. quit\n")
        if int(action) == 1:
            name = input('name: ')
            price = input('price: ')
            quantity = input('quantity: ')
            category = input('category: ')
            threshold = input('threshold: ')
            amount = input('amount sold: ')
            add_product( name, price, quantity, category, threshold, amount)
            print('PRODUCT ADDED\n')
        elif int(action) == 2:
            name = input('name of product to be removed: ')
            remove_product(name)
        elif int(action) == 3:
            name = input('name of product to be updated: ')
            quantity = input('new quantity: ')
            amount = input('amount of product sold(if none type 0): ')
            update_product(name, quantity, amount)
        elif int(action) == 4:
            display()
        elif int(action) == 5:
            name = input("name of product you're looking for: ")
            search(name)
        elif int(action) == 6:
            display_sales_table()
        elif int(action) == 7:
            sys.exit()
else:
    sys.exit()
    