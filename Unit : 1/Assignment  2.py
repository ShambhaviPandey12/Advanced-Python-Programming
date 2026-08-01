
def bill_header(func):
    def wrapper(*args, **kwargs):
        print("-" * 40)
        print("   CITY MART BILL")
        print("-" * 40)
        func(*args, **kwargs)
        print("-" * 40)
    return wrapper


class Bill:
    shop_name = "City Mart"

    
    def __init__(self, customer, item, amount):
        self.customer = customer
        self.item = item
        self.amount = amount

    
    @classmethod
    def change_shop_name(cls, new_name):
        cls.shop_name = new_name

    
    def __str__(self):
        return f"Customer : {self.customer}\nItem : {self.item}\nAmount : {self.amount}"

    
    @bill_header
    def show_bill(self):
        print("Shop :", Bill.shop_name)
        print(self)
        if self.amount >= 1000:
            print("Discount : 10%")
        else:
            print("Discount : None")

bill1 = Bill("Rahul", "Grocery", 1200)
bill1.show_bill()

print()


Bill.change_shop_name("City Mart - Branch 2")
bill2 = Bill("Priya", "Stationery", 500)
bill2.show_bill()

#Output
'''----------------------------------------
   CITY MART BILL
----------------------------------------
Shop : City Mart
Customer : Rahul
Item : Grocery
Amount : 1200
Discount : 10%
----------------------------------------

----------------------------------------
   CITY MART BILL
----------------------------------------
Shop : City Mart - Branch 2
Customer : Priya
Item : Stationery
Amount : 500
Discount : None
----------------------------------------'''