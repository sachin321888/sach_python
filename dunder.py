import  datetime
class Product:
    mydate = datetime.datetime(2023, 1, 27, 9, 50, 37, 429078)
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return (f"The name is {self.name} and price is {self.price} with {self.category} category on date {Product.mydate}")

    def __repr__(self):
            return (f"The detailed name is {self.name} and price is {self.price} with {self.category} category on date {Product.mydate}")

# Create a product
laptop = Product("MacBook Pro", 1999.99, "Electronics")

# print(laptop)

print("str() output:", str(Product.mydate))
print("repr() output:", repr(Product.mydate))
