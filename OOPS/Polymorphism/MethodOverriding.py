
class Person:

    """
    A class represents a Person.

    Attributes
    ----------
    name : str
        Name of the Person.

    age : int
        Age of the Person.

    gender: str
        Gender of the Person.

    Methods
    -------
    display():
        Returns a string contains name, age, gender of the Person.
    """

    def __init__(self, name: str, age: int, gender: str) -> None:
        """
        Parameters
        ----------
        name : str
            Name of the Person.

        age : int
            Age of the Person.

        gender: str
            Gender of the Person.
        """
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        """
        Returns
        -------
        str
            Returns a string contains name, age, gender of the Person.
        """
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"
    

class Employee(Person):
    """
    A class represents an Employee.

    Attributes
    ----------
    name : str
        Name of the Employee.

    id : int
        Id of the Employee.

    age : int
        Age of the Employee.

    gender: str
        Gender of the Employee.

    Methods
    -------
    display():
        Returns a string contains name, id, age, gender of the Employee.
    """

    def __init__(self, name: str, id: int, age: int, gender: str) -> None:
        """
        Parameters
        ----------
        name : str
            Name of the Employee.

        age : int
            Age of the Employee.

        gender: str
            Gender of the Employee.
        """
        super().__init__(name, age, gender)
        self.id = id

    def display(self):
        """
        Returns
        -------
        str
            Returns a string contains name, id, age, gender of the Employee.
        """
        return f"{super().display()}, Id: {self.id}"
    
if __name__ == '__main__':

    person = Person("Siva", 25, "Male")
    print(person.display())

    employee = Employee("Siva",1, 25, "Male")
    print(employee.display())