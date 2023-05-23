class Cart:
    def __init__(self):
        self.Products=[]
    def add_to_cart(self,product):
        self.Products.append(product)
    def show_cart(self):
        for product in self.Products:
            print(product.Name, product.Quantity, product.Price)
        