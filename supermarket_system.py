class Product(object):
    def __init__(self,name,price):
        self.name = name 
        self.price = price

class Cart(object):
    def __init__(self):
        self.items = []
    
    def add_item(self,item):
        self.items.append(item)
    
    def remove_item(self,item):
        self.items.remove(item)
    
    def get_total(self):
        total = 0 
        for item in self.items:
            total += item.price
        return total

class Supermarket(object):
    def __init__(self):
        self.products = []
        self.cart = Cart()
    
    def add_product(self,product):
        self.products.append(product)
    
    def list_products(self):
        print("All Products : ")
        for i , product in enumerate(self.products):
            print(f"{str(i+1)}. {product.name} - ${product.price}")
    
    def shopping(self):
        while True:
            self.list_products()
            print("0. Exit")
            choice = int(input("Enter your choice : "))
            if choice == 0:
                break
            if choice in range(1,len(self.products)+1):
                product = self.products[choice-1]
                print(f"You have selected {product.name} for ${product.price}")
                add_to_cart = input("Do you want to add this to your cart? (y/n) : ")
                if add_to_cart == "y":
                    self.cart.add_item(product)
                    print(f"{product.name} added to your cart successfully ..")
                else:
                    print("Okay.")
            else:
                print("Invalid choice. Try again.")
        if self.cart.items:
            print("\nYour Cart: ")
            for i ,item in enumerate(self.cart.items):
                print(f"{str(i+1)}. {item.name} - ${item.price}")
            print(f"Total: ${round(self.cart.get_total(),2)}")
        else:
            print("Your cart is empty.")
                
sm = Supermarket()
sm.add_product(Product("Apple",0.99))
sm.add_product(Product("Book",1.23))
sm.add_product(Product("banana",0.53))
sm.add_product(Product("Pepci",1.99))
sm.shopping()
    
