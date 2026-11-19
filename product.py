class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_final_price(self, discount):
        return self.price - (self.price * discount / 100)
