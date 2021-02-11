class Product:
    # Constructor
    def __init__(self, name, price):
        # Object attributes
        self.name = name
        self.price = price

    # Methods
    def netprice(self):
        return self.price + self.price * 0.12

    def print_details(self):
        print('Name      : ', self.name)
        print("Price     : ", self.price)
        print("Net price : ", self.netprice())


p = Product("Dell Laptop", 60000)  # Object
p.print_details()

p2 = Product("IPad", 40000)
p2.print_details()
