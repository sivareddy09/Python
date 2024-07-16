

class Animal:

    """
        A class used to represent an Animal.

    Attributes
    ----------
    name: str
        Name of the Animal

    Methods
    -------
    speak()
        Returns a string with the name of the animal and can speak

    walk()
        Returns a string with the name of the animal and can walk
    """

    def __init__(self, name: str):
        """
        Parameters
        ----------
        name: str
            Name of the Animal
        """
        self.name = name

    def speak(self):
        """
        Returns
        -------
        str
            Returns a string with the name of the animal and can speak
        """
        return f"{self.name} can speak"
    
    def walk(self):
        """
        Returns
        -------
        str
            Returns a string with the name of the animal and can walk
        """
        return f"{self.name} can walk"
    

class Dog(Animal):

    """
        A class used to represent a Dog.

    Attributes
    ----------
    name: str
        Name of the Dog

    Methods
    -------
    speak()
        Returns a string with the name of the Dog and dog sound

    walk()
        Returns a string with the name of the Dog and can walk
    """

    def __init__(self, name: str):
        """
        Parameters
        ----------
        name: str
            Name of the Dog
        """
        super().__init__(name)

    def speak(self):
        """
        Returns
        -------
        str
            Returns a string with the name of the Dog and dog sound
        """
        return f"{self.name} can bow boww"
    
    def walk(self):
        """
        Returns
        -------
        str
            Returns a string with the name of the Dog and can walk
        """
        return f"{self.name} can walk"
    

class Cat(Animal):

    """
        A class used to represent a Cat.

    Attributes
    ----------
    name: str
        Name of the Cat

    Methods
    -------
    speak()
        Returns a string with the name of the Cat and can speak

    walk()
        Returns a string with the name of the Cat and cat sound
    """

    def __init__(self, name: str):
        """
        Parameters
        ----------
        name: str
            Name of the Cat
        """
        super().__init__(name)

    def speak(self):
        """
        Returns
        -------
        str
            Returns a string with the name of the Cat and cat sound
        """
        return f"{self.name} can meow meow"
    
    def walk(self):
        """
        Returns
        -------
        str
            Returns a string with the name of the Cat and can walk
        """
        return f"{self.name} can walk"
    

if __name__ == '__main__':

    animal = Animal("Dog")
    print(animal.speak())
    print(animal.walk())

    dog = Dog("Watcher")
    print(dog.speak())
    print(dog.walk())

    cat = Cat("Whisky")
    print(cat.speak())
    print(cat.walk())