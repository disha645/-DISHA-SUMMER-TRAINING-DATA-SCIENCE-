#bank management
class bank:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self):
        self.balance +=2000
        print(f"Deposited {2000}. New balance is {self.balance}.")

    def withdraw(self):
        if 2000 > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= 2000
            print(f"Withdrew {2000}. New balance is {self.balance}.")

    def display_balance(self):
        print(f"Account holder: {self.name}, Account number: {self.account_number}, Balance: {self.balance}")
    
s1 = bank("Disha", 123456789, 10000)
s1.display_balance()
s1.deposit()
s1.withdraw()

#Q1. Create a class Product with attributes product_id and price. Implement methods to get the product details.
class Product :
    def __init__(self,product_id,price):
     self.__product_id = product_id 
     self.__price = price
    def get_product_id(self):
       return self.__product_id
    def get_price(self):
       return self.__price

#inheritance
class Electronics(Product):
   __product_id__="p231",
   __price__=20000
   def calculate_discount(self):
      discount=self.get_price()*0.10
      final_price=self.get_price()-discount
      return final_price
class clothing(Product):
   __product_id__="p232",
   __price__=1000
   def calculate_discount(self):
      discount=self.get_price()*0.20
      final_price=self.get_price()-discount
      return final_price
class grocery(Product):
   __product_id__="p233",
   __price__=500
   def calculate_discount(self):
      discount=self.get_price()*0.05
      final_price=self.get_price()-discount
      return final_price
product1=Electronics("p231", 20000)
product2=clothing("p232", 1000)
product3=grocery("p233", 500)
print("Electronics - Product ID:", product1.get_product_id())
print("Electronics - Price:", product1.get_price())
print("Electronics - Final price:", product1.calculate_discount())

print("\nClothing - Product ID:", product2.get_product_id())
print("Clothing - Price:", product2.get_price())
print("Clothing - Final price:", product2.calculate_discount())

print("\nGrocery - Product ID:", product3.get_product_id())
print("Grocery - Price:", product3.get_price())
print("Grocery - Final price:", product3.calculate_discount())