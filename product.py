class Product:
    def __init__(self,Name, Quantity, Price):
        self.Name=Name
        self.Quantity=Quantity
        self.Price=Price

    def show(self):
        print(self.Name, self.Quantity, self.Price)