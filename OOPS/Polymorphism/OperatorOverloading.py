

class Person:

    """
    A class represent a Person.

    Attributes
    ----------
    name : str
        Name of the Person.
    
    age : int
        Age of the Person.

    other : any
        other object input

    Methods
    -------
    __gt__():
        note: overloading the method by giving new definition
        Return a value by adding them based on the inputs given 
    """

    def __init__(self, name: str, age:int) -> None:
        """
        Parameters
        ----------
        name : str
            Name of the Person.
        
        age : int
            Age of the Person.
        """
        self.name = name
        self.age = age
    
    def __gt__(self, other: any):
        """
        Parameters
        ----------
        other : any
            Another objects value
        """
        return self.age > other.age
    

if __name__ == '__main__':
    person1 = Person("Siva", 25)
    person2 = Person("Vijay", 23)

    if person1 > person2:
        print(f"{person1.name} will pay the bill")
    else:
        print(f"{person2.name} will pay the bill")
