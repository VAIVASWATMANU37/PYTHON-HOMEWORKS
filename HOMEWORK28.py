#Normal Writing Editon
class Vehicle:
    def __init__(self, fare):
        self.fare = fare
    def get_fare(self):
        return self.fare
class Bus(Vehicle):
    def __init__(self, fare, discount=0.10):
        super().__init__(fare)
        self.discount = discount
    def calculate_fare(self):
        final_fare = self.fare - (self.fare * self.discount)
        return final_fare
vehicle = Vehicle(100)
bus = Bus(100)
print("Vehicle Fare:", vehicle.get_fare())
print("Bus Fare:", bus.calculate_fare())