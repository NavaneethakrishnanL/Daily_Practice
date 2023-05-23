from product import Product
from cart import Cart
product1=Product("Apple", 20, 200)
cart1=Cart()
cart1.add_to_cart(product1)
# product1.show()
cart1.show_cart()
