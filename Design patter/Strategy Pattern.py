from abc import ABC, abstractmethod

# Strategy Interface
class DeliveryStrategy(ABC):
    @abstractmethod
    def deliver(self, order_id):
        pass


# Concrete Strategies
class BikeDelivery(DeliveryStrategy):
    def deliver(self, order_id):
        print(f"Order {order_id} delivered by Bike")


class DroneDelivery(DeliveryStrategy):
    def deliver(self, order_id):
        print(f"Order {order_id} delivered by Drone")


class WalkDelivery(DeliveryStrategy):
    def deliver(self, order_id):
        print(f"Order {order_id} delivered by Walk")


# Context
class DeliveryService:
    def __init__(self, strategy):
        self.strategy = strategy

    def dispatch(self, order_id):
        self.strategy.deliver(order_id)


# Client Code
service = DeliveryService(BikeDelivery())
service.dispatch(101)

service = DeliveryService(DroneDelivery())
service.dispatch(102)

service = DeliveryService(WalkDelivery())
service.dispatch(103)

# Output 
'''Order 101 delivered by Bike
Order 102 delivered by Drone
Order 103 delivered by Walk'''