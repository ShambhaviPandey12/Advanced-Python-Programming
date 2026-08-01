from abc import ABC, abstractmethod

class ShippingStrategy(ABC):
    @abstractmethod
    def ship(self, weight):
        pass


class StandardShipping(ShippingStrategy):
    def ship(self, weight):
        print(f"Package of {weight}kg sent using Standard Shipping.")


class ExpressShipping(ShippingStrategy):
    def ship(self, weight):
        print(f"Package of {weight}kg sent using Express Shipping.")


class DroneShipping(ShippingStrategy):
    def ship(self, weight):
        print(f"Package of {weight}kg sent using Drone Shipping.")


class ShippingService:
    def __init__(self, strategy=None):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def deliver(self, weight):
        if self.strategy is None:
            print("Please select a shipping method.")
        else:
            self.strategy.ship(weight)


service = ShippingService()

while True:
    print("\n===== Shipping Service System =====")
    print("1. Standard Shipping")
    print("2. Express Shipping")
    print("3. Drone Shipping")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 4:
        print("Thank you for using the Shipping System!")
        break

    weight = float(input("Enter package weight in kg: "))

    if choice == 1:
        service.set_strategy(StandardShipping())
    elif choice == 2:
        service.set_strategy(ExpressShipping())
    elif choice == 3:
        service.set_strategy(DroneShipping())
    else:
        print("Invalid choice!")
        continue

    service.deliver(weight)

#Output
'''===== Shipping Service System =====
1. Standard Shipping
2. Express Shipping
3. Drone Shipping
4. Exit
Enter your choice: 1
Enter package weight in kg: 5
Package of 5.0kg sent using Standard Shipping.

===== Shipping Service System =====
1. Standard Shipping
2. Express Shipping
3. Drone Shipping
4. Exit
Enter your choice: 3
Enter package weight in kg: 2
Package of 2.0kg sent using Drone Shipping.

===== Shipping Service System =====
1. Standard Shipping
2. Express Shipping
3. Drone Shipping
4. Exit
Enter your choice: 4
Thank you for using the Shipping System!'''