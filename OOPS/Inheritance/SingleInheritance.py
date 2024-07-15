
class Person:
    
    """
    A class used to represent a Person.
    
    Attributes
    ----------
    name : str
        Name of the Person.
    age : int
        Age of the Person
    gender : str
        Gender of the Person
    email : str
        Email of the Person
    phoneNumber : int
        Phone Number of the Person
    address : str
        Address of the Person
    Methods
    -------
    getDetails():
        Returns a string containing all the details name, age, gender, email, phoneNumber, address of a Person.
    """

    def __init__(self, name: str, age: int, gender: str, email: str, phoneNumber: int, address: str) -> None:
        """
        Parameters
        ----------
        name : str
            Name of the Person.
        age : int
            Age of the Person
        gender : str
            Gender of the Person
        email : str
            Email of the Person
        phoneNumber : int
            Phone Number of the Person
        address : str
            Address of the Person
        """
        self.name = name
        self.age = age
        self.gender = gender
        self.email = email
        self.phoneNumber = phoneNumber
        self.address = address

    def getDetails(self) -> str:
        """
        Returns
        -------
        str
            Returns a string containing all the details name, age, gender, email, phoneNumber, address of a Person.
        """
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Email: {self.email}, Phone Number: {self.phoneNumber}, Address: {self.address}"
    

class Employee(Person):
    """
    A class used to represent a Employee(Child Class). Which is Inherited by Person(Parent Class).
    
    Attributes
    ----------
    name : str
        Name of the Employee.
    empId : int
        Employee Id of the Employee.
    age : int
        Age of the Employee.
    gender : str
        Gender of the Employee.
    email : str
        Email of the Employee.
    phoneNumber : int
        Phone Number of the Employee.
    address : str
        Address of the Employee.

    Methods
    -------
    getDetails():
        Returns a string containing all the details empId, name, age, gender, email, phoneNumber, address of an Employee.
    """

    def __init__(self, name: int, empId: int, age: int, gender: str, email: str, phoneNumber: int, address: str):
        """
        Parameters
        ----------
        name : str
            Name of the Employee.
        empId : int
            Employee Id of the Employee.
        age : int
            Age of the Employee.
        gender : str
            Gender of the Employee.
        email : str
            Email of the Employee.
        phoneNumber : int
            Phone Number of the Employee.
        address : str
            Address of the Employee.
        """

        super().__init__(name, age, gender, email, phoneNumber, address)
        self.empId = empId

    def getDetails(self):
        """
        Returns
        -------
        str
            Returns a string containing all the details empId, name, age, gender, email, phoneNumber, address of an Employee.
        """
        return f"EmpId: {self.empId}, {super().getDetails()}"

if __name__ == '__main__':
    person = Person("Siva", 25, "Male", "gspr991@gmail.com", 9640718354, "Rajampet")
    print(person.getDetails())

    employee = Employee("Siva", 439, 25, "Male", "gspr991@gmail.com", 9640718354, "Rajampet")
    print(employee.getDetails())