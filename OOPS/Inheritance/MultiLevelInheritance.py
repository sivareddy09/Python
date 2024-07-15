
class Vehicle:

    def __init__(self, brand, model, makeYear, type) -> None:
        self.brand = brand
        self.model = model
        self.makeYear = makeYear
        self.type = type

    def getDetails(self):
        return f"Brand: {self.brand}, Model: {self.model}, Year of Manufacture: {self.makeYear}, Type: {self.type}"
    
class Car(Vehicle):

    def __init__(self, brand, model, makeYear, type) -> None:
        super().__init__(brand, model, makeYear, type)
        self.vehicleType = "Car"

    def getDetails(self):
        return f"{super().getDetails()}, VehicleType: {self.vehicleType}"

class ElectricCar(Car):

    def __init__(self, brand, model, makeYear, type) -> None:
        super().__init__(brand, model, makeYear, type)
        self.vehicleType = "Electric Car"



if __name__ == '__main__':
    vehicle = Vehicle("Royal Enfield", "Continental GT 650", 2023, "Petrol")
    print(vehicle.getDetails())
    car = Car("Royal Enfield", "Continental GT 650", 2023, "Petrol")
    print(car.getDetails())
    electricCar = ElectricCar("Royal Enfield", "Continental GT 650", 2023, "Petrol")
    print(electricCar.getDetails())