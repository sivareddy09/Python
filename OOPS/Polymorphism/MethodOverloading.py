
class Addition:

    """
    A class to perform addition operations.

    Methods
    -------
    add(input1, input2)
        Adds two inputs.

    add(input1, input2, input3)
        Adds three inputs.
    """

    def add(self, input1: any, input2: any):
        """
        Adds two inputs.

        Parameters
        ----------
        input1 : int or float
            The first input value.
        input2 : int or float
            The second input value.

        Returns
        -------
        int or float
            The sum of the two input values.
        """
        return input1+input2
    
    def add(self, input1: any, input2: any, input3: any):
        """
        Adds three inputs.

        Parameters
        ----------
        input1 : int or float
            The first input value.
        input2 : int or float
            The second input value.
        input3 : int or float
            The third input value.

        Returns
        -------
        int or float
            The sum of the three input values.
        """
        return input1+input2+input3
    

class AdditionWorks:
    """
    A class to perform addition operations.

    Methods
    -------
    add(*args)
        Adds a variable number of inputs.
    """

    def add(self, *args):
        """
        Adds a variable number of inputs.

        Parameters
        ----------
        *args : int or float
            The input values to be added.

        Returns
        -------
        int or float
            The sum of the input values.
        """
        total = 0
        for i in args:
            total+=i
        return total
    

if __name__ == '__main__':
    addition = Addition()
    print(addition.add(1, 2, 3))
    # the below code will throw an error saying one argument is missing
    # print(Addition().add(1, 2))

    additionworks = AdditionWorks()
    print(additionworks.add(1, 3))
    print(additionworks.add(1, 2, 3))

    
            