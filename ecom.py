class Products:
    def __init__(self, pdt_id, pdt_name, pdt_price, order_date):
        self.pdt_id = pdt_id
        self.pdt_name = pdt_name
        self.pdt_price = pdt_price
        self.order_date = order_date

    def add_to_cart(self):
        print("PRODUCT DETAILS")
        print("-----------------")
        print("Product_id:", self.pdt_id)
        print("Product :", self.pdt_name)
        print("Price:", self.pdt_price)


class Customers:
    def __init__(self, c_name, c_country):
        self.c_name = c_name
        self.c_country = c_country

    def customer_details(self):
        print("\nCUSTOMER DETAILS")
        print("-----------------")
        print("Name:", self.c_name, "From", self.c_country)


def Ordered_placed(pdt_id, pdt_name, pdt_price, order_date, c_name, c_country):
    print("\nORDER PLACED:")
    print("-----------------")
    print("The", pdt_name, "[ID-NO:", pdt_id, "] is ordered by", c_name, "from", c_country, "for Rs.", pdt_price, "on",
          order_date)


class Orders:
    def __init__(self, product, customer):
        self.product = product
        self.customer = customer


pdt_obj = Products("N1125", "Nike shoe", "1650", "12/march/2024")
cus_obt = Customers("Priya", "India")
Order_obj = Orders(pdt_obj, cus_obt)
pdt_obj.add_to_cart()
cus_obt.customer_details()
Ordered_placed(Order_obj.product.pdt_id,
               Order_obj.product.pdt_name,
               Order_obj.product.pdt_price,
               Order_obj.product.order_date,
               Order_obj.customer.c_name,
               Order_obj.customer.c_country)
