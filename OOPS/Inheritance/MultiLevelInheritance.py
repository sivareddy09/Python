
class Vehicle:

    """
    A class used to represent a Vehicle.
    
    Attributes
    ----------
    brand : str
        Brand of the Vehicle.
    model : str
        Model of the Vehicle.
    makeYear : int
        Manufactured Year of the Vehicle.
    type : str
        Type of the Vehicle.

    Methods
    -------
    getDetails():
        Returns a string containing all the details brand, model, makeYear, Type of Vehicle.
    """

    def __init__(self, brand: str, model: str, makeYear: int, type: str) -> None:
        """
        Parameters
        ----------
        brand : str
            Brand of the Vehicle.
        model : str
            Model of the Vehicle.
        makeYear : int
            Manufactured Year of the Vehicle.
        type : str
            Type of the Vehicle.
        """
        self.brand = brand
        self.model = model
        self.makeYear = makeYear
        self.type = type

    def getDetails(self):
        """
        Returns
        -------
        str
            Returns a string containing all the details brand, model, makeYear, Type of Vehicle.
        """
        return f"Brand: {self.brand}, Model: {self.model}, Year of Manufacture: {self.makeYear}, Type: {self.type}"
    
class Car(Vehicle):

    """
    A class used to represent a Car(Child Class). Which is Inherited by Vehicle(Parent Class).
    
    Attributes
    ----------
    brand : str
        Brand of the Vehicle.
    model : str
        Model of the Vehicle.
    makeYear : int
        Manufactured Year of the Vehicle.
    type : str
        Type of the Vehicle.

    Methods
    -------
    getDetails():
        Returns a string containing all the details brand, model, makeYear, Type of Vehicle.
    """

    def __init__(self, brand: str, model: str, makeYear: int, type: str) -> None:
        """
        Parameters
        ----------
        brand : str
            Brand of the Vehicle.
        model : str
            Model of the Vehicle.
        makeYear : int
            Manufactured Year of the Vehicle.
        type : str
        """
        super().__init__(brand, model, makeYear, type)

class ElectricCar(Car):
    """
    A class used to represent a ElectricCar(Child Class). Which is Inherited by Car(Parent Class).
    
    Attributes
    ----------
    brand : str
        Brand of the Vehicle.
    model : str
        Model of the Vehicle.
    makeYear : int
        Manufactured Year of the Vehicle.
    type : str
        Type of the Vehicle.

    Methods
    -------
    getDetails():
        Returns a string containing all the details brand, model, makeYear, Type of Vehicle.
    """

    def __init__(self, brand, model, makeYear, type) -> None:
        """
        Parameters
        ----------
        brand : str
            Brand of the Vehicle.
        model : str
            Model of the Vehicle.
        makeYear : int
            Manufactured Year of the Vehicle.
        type : str
            Type of the Vehicle.
        """
        super().__init__(brand, model, makeYear, type)



if __name__ == '__main__':
    vehicle = Vehicle("Royal Enfield", "Continental GT 650", 2023, "Petrol")
    print(vehicle.getDetails())
    car = Car("Royal Enfield", "Continental GT 650", 2023, "Petrol")
    print(car.getDetails())
    electricCar = ElectricCar("Royal Enfield", "Continental GT 650", 2023, "Petrol")
    print(electricCar.getDetails())