

class Add:

    """
    A class used to represent Additon of two values.
    
    Attributes
    ----------
    input1 : any
        input1 for the Addition.
    input2 : any
        input2 for the Addition.

    Methods
    -------
    addition():
        Returns a value depends on the inputs given by adding them.
    """

    def __init__(self, input1: any, input2: any):
        """
        Parameters
        ----------
        input1 : any
            input1 for the Addition.
        input2 : any
            input2 for the Addition.
        """
        self.input1 = input1
        self.input2 = input2

    def addition(self):
        """
        Returns
        -------
        any
            Returns a value depends on the inputs given by adding them.
        """
        return self.input1+self.input2
    
class Sub:

    """
    A class used to represent Substraction of two values.
    
    Attributes
    ----------
    input1 : any
        input1 for the Substraction.
    input2 : any
        input2 for the Substraction.

    Methods
    -------
    substraction():
        Returns a value depends on the inputs given by substracting them.
    """

    def __init__(self, input1: any, input2: any):
        """
        Parameters
        ----------
        input1 : any
            input1 for the Substraction.
        input2 : any
            input2 for the Substraction.
        """
        self.input1 = input1
        self.input2 = input2

    def substraction(self):
        """
        Returns
        -------
        any
            Returns a value depends on the inputs given by substracting them.
        """
        return self.input1-self.input2
    
class Calculation(Add, Sub):
    """
    A class used to represent Calculating the two values.
    
    Attributes
    ----------
    input1 : any
        input1 for the Calculation.
    input2 : any
        input2 for the Calculation.

    Methods
    -------
    addition():
        Returns a value depends on the inputs given by substracting them.
    addition():
        Returns a value depends on the inputs given by substracting them.
    """    

    def __init__(self, input1: any, input2: any):
        """
        Parameters
        ----------
        input1 : any
            input1 for the Calculation.
        input2 : any
            input2 for the Calculation.
        """
        super().__init__(input1, input2)

    def __add__(self, other):
        return Calculation(self.input1+other.input1, self.input2+other.input2)
    
    def __str__(self) -> str:
        return f"Calculation(Input1: {self.input1}, Input2: {self.input2})"


if __name__ == '__main__':

    add = Add(1, 2)
    print(add.addition())

    sub = Sub(4, 2)
    print(sub.substraction())

    calculation = Calculation(4, 2)
    print(calculation.addition())
    print(calculation.substraction())

    calculation1 = Calculation(4, 2)
    calculation2 = Calculation(1, 1)
    print(calculation1.__add__(calculation2))