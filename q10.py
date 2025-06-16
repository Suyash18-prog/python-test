# Demonstrate single and multilevel inheritance using vehicle -> car -> electric car classes.

class Vehicle:
    def __init__(self,name,seat_number):
        self.name =name
        self.seat_number=seat_number

    def info(self):
        print(f"Name = {self.name}")
        print(f"Number of seat = {self.seat_number}")

class Car(Vehicle):#single
    def __init__(self,name,seat_number,fuel_type):
        super().__init__(name,seat_number)
        self.fuel_type=fuel_type

    def info(self):
        print(f"Name = {self.name}")
        print(f"Number of seat = {self.seat_number}")
        print(f"Fuel type = {self.fuel_type}")

class ElectricCar(Car):#multilevel
    def __init__(self,name,seat_number,fuel_type,is_automated):
        super().__init__(name,seat_number,fuel_type)
        self.is_automated = is_automated

    def info(self):
        print(f"Name = {self.name}")
        print(f"Number of seat = {self.seat_number}")
        print(f"Fuel type = {self.fuel_type}")
        print(f"Is automatic = {self.is_automated}")


Car_1 = Car('Thar',4,'petrol')
car_2 = ElectricCar("Tesla",4,"Electric","yes")
Car_1.info()
car_2.info()