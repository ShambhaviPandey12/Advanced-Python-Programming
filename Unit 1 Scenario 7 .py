class Product:
    def __init__(self, product_id, product_name, price):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price

        # Categorize product
        if self.price >= 10000:
            self.category = "Expensive"
        else:
            self.category = "Affordable"


class Inventory:
    def __init__(self):
        self.products = []

    # Add product
    def add_product(self, product):
        self.products.append(product)

    # Display all products
    def display_products(self):
        print("\n--- Product Inventory ---")

        for product in self.products:
            print("Product ID:", product.product_id)
            print("Product Name:", product.product_name)
            print("Price: ₹", product.price)
            print("Category:", product.category)
            print("-------------------------")


# Create products
p1 = Product(101, "Laptop", 50000)
p2 = Product(102, "Mouse", 800)
p3 = Product(103, "Headphones", 5000)

# Create inventory
inventory = Inventory()

# Add products to inventory
inventory.add_product(p1)
inventory.add_product(p2)
inventory.add_product(p3)

# Display products
inventory.display_products()