from abc import ABC, abstractmethod

class Person(ABC):

    """
    A class represents a Person.

    Attributes
    ---------
    name : str
        Name of the Person.
    age(private) : int
        Age of the Person.
    gender(protected) : str
        Gender of the Person.
    
    Methods
    -------
    eat(): abstrct method
        Returns a string containg the person is eating or not.
    sleep(): abstract method
        Returns a string containg the person is sleeping or not.
    work(): abstract method
        Returns a string containg the person is working or not.
    display()
        Returns a string containing name, age, gender of the person.
    
    """

    def __init__(self, name, age, gender):
        """
        Parameters
        ---------
        name : str
            Name of the Person.
        age(private) : int
            Age of the Person.
        gender(protected) : str
            Gender of the Person.
        """
        self.name = name
        self.__age = age
        self._gender = gender

    @abstractmethod
    def eat(self):
        """
        Returns
        -------
        str
            Returns a string containg the person is eating or not.
        """
        pass

    @abstractmethod
    def sleep(self):
        """
        Returns
        -------
        str
            Returns a string containg the person is sleeping or not.
        """
        pass

    @abstractmethod
    def work(self):
        """
        Returns
        -------
        str
            Returns a string containg the person is working or not.
        """
        pass

    # Concrete Method
    def display(self):
        """
        Returns
        -------
        str
            Returns a string containing name, age, gender of the person.
        """
        return f"Name: {self.name}, Age: {self.__age}, Gender: {self._gender}"


class Employee(Person):

    """
    A class represents a Employee.

    Attributes
    ---------
    name : str
        Name of the Employee.
    age(private) : int
        Age of the Employee.
    gender(protected) : str
        Gender of the Employee.
    
    Methods
    -------
    eat(): abstrct method
        Returns a string containg the Employee is eating or not.
    sleep(): abstract method
        Returns a string containg the Employee is sleeping or not.
    work(): abstract method
        Returns a string containg the Employee is working or not.
    display()
        Returns a string containing name, age, gender of the Employee.
    
    """

    def __init__(self, name, id, age, gender):
        """
        Parameters
        ---------
        name : str
            Name of the Employee.
        id : int
            Id of the Employee.
        age(private) : int
            Age of the Employee.
        gender(protected) : str
            Gender of the Employee.
        """
        super().__init__(name, age, gender)
        self.__id = id

    def eat(self):
        """
        Returns
        -------
        str
            Returns a string containg the name and Employee is working or not.
        """
        return f"{self.name} is eating."
    
    def sleep(self):
        """
        Returns
        -------
        str
            Returns a string containg the name and Employee is working or not.
        """
        return f"{self.name} is sleeping."
    
    def work(self):
        """
        Returns
        -------
        str
            Returns a string containg the name and Employee is working or not.
        """
        return f"{self.name} is working."

    def display(self):
        """
        Returns
        -------
        str
            Returns a string containing name, age, gender, id of the Employee.
        """
        return f"{super().display()}, Id: {self.__id}"
    

if __name__ == '__main__':
    # person = Person("Siva", 25, "Male")
    # print(person.display())

    employee = Employee("Siva", 439, 25, "Male")
    # will throw error because age is declared as private
    # print(employee.__age)
    # print(employee.__id)

    # will not throw error but it is bad idea to use outside the class
    # print(employee._gender)

    print(employee.display())
    print(employee.eat())
    print(employee.sleep())
    print(employee.work())