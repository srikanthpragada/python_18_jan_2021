class Product:
    # Constructor
    def __init__(self, name, price):
        # Object attributes
        self.name = name
        self.__price = price  # Private

    # Methods
    def netprice(self):
        return self.__price + self.__price * 0.12

    def print_details(self):
        print('Name      : ', self.name)
        print("Price     : ", self.__price)
        print("Net price : ", self.netprice())


p = Product("Dell Laptop", 60000)  # Create an object
p._Product__price = 0
print(p.__dict__)
p.print_details()

p2 = Product("IPad", 40000)
p2.print_details()
