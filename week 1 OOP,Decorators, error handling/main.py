# How to create a class:
class Item:
    def calculate_total_price(self, x, y):
        return x * y

# How to create an instance of a class
item1 = Item()

# Assign attributes:
item1.name = "milk"
item1.price = 78
item1.quantity = 5

# Calling methods from instances of a class:
print(item1.calculate_total_price(item1.price, item1.quantity))

# How to create an instance of a class (We could create as much as instances we'd like to)
item2 = Item()

# Assign attributes
item2.name = "oil"
item2.price = 120
item2.quantity = 3

# Calling methods from instances of a class: 
print(item2.calculate_total_price(item2.price, item2.quantity))