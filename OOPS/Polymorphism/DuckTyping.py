

class Duck:

    """
    A class represnt a Duck.

    Methods
    -------
    swim():
        Return a string by saying duck can swim or not.

    speaks():
        Returns a string by saying how duck can speak or cannot speak. 
    """

    def swim(self) -> str:
        """
        Returns
        -------
        str
            Return a string by saying duck can swim or not.
        """
        return "I am a duck and i can swim."
    
    def speaks(self) -> str:
        """
        Returns
        -------
        str
            Returns a string by saying how duck can speak or cannot speak. 
        """
        return "kwak kwak kwakkk."
    
class Dog:
    """
    A class represnt a Dog.

    Methods
    -------
    swim():
        Return a string by saying dog can swim or not.

    speaks():
        Returns a string by saying how dog can speak or cannot speak. 
    """

    def swim(self) -> str:
        """
        Returns
        -------
        str
            Return a string by saying dog can swim or not.
        """
        return "I am a dog and i can swim."
    
    def speaks(self) -> str:
        """
        Returns
        -------
        str
            Returns a string by saying how dog can speak or cannot speak. 
        """
        return "bow bow bowww."
    
class Person:
    """
    A class represnt a Person.

    Methods
    -------
    speaks():
        Returns a string by saying how person can speak or cannot speak. 
    """

    def speaks(self) -> str:
        """
        Returns
        -------
        str
            Returns a string by saying how person can speak or cannot speak. 
        """
        return "blah blah blahhh."
    
class TestDuckTyping:

    """
    A class represent testing the DuckTyping technique.

    Attributes
    ----------
    obj : int
        attribute of the TestDuckTyping which will acts as a object of the given class.

    Methods
    -------
    display():
        Prints a string contains the object's method output if the method is present for the object given or returns method not defined for the given object.
    """

    def __init__(self, obj):
        """
        Parameters
        -----------
        obj : int
            attribute of the TestDuckTyping which will acts as a object of the given class.
        ----------
        """
        self.obj = obj

    def diplay(self):
        """
        Returns
        -------
        str
            Prints a string contains the object's method output if the method is present for the object given or returns method not defined for the given object.
        """
        print(self.obj.swim())
        print(self.obj.speaks())
        print("Done.")


if __name__ == '__main__':
    duck = Duck()
    dog = Dog()
    person = Person()
    TestDuckTyping(duck).diplay()
    TestDuckTyping(dog).diplay()
    TestDuckTyping(person).diplay()