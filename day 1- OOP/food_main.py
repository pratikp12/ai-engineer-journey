#class define

class food:
   all = []
   def __init__(self,name: str, price: float, quantity=0):
       # Run validations to the received arguments
       assert price >= 0, f"Price {price} is not greater than or equal to zero!"
       assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

       print(f"A instance created for {name}")
       # Assign to self object
       self.name = name
       self.price = price
       self.quantity = quantity
       
       # Actions to execute
       food.all.append(self)
   
   def calculate_total_price(self):
        return print(f"Total price will be {self.price * self.quantity}")
       
   
   
   def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


milk=food('milk',79.0,3)
mango=food('mango',50.0,12)

#milk.calculate_total_price()
print(food.all)
