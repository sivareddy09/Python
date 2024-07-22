from Person import Person
from random import randint
class Employee(Person):

    def __init__(self, firstName, lastName, gender, age) -> None:
        super().__init__(firstName, lastName, gender, age)
        self.__id = self.generateEmployeeId()

    def display(self):
        return f"{super().display()}, EmployeeId: {self.__id}"
    
    def generateEmployeeId(self):
        return f"{self.__getPartOfName(self.firstName, 4)+self.__getPartOfName(self.lastName, 4)+str(randint(0, 1000))}"
    
    def __getPartOfName(self, name, numOfCharacters):
        if len(name) <= numOfCharacters:
            return str(name+self.generateX(numOfCharacters-len(name)))
        return str(name[0:numOfCharacters])

    def generateX(self, value):
        return 'X'*value
    
if __name__ == '__main__':
    emp = Employee("SivaPrasadReddy", "Geddam", "Male", 25)
    print(emp.display())
    # print(emp.generateEmployeeId())
    
    emp1 = Employee("Si", "Ge", "Male", 25)
    print(emp1.display())
    # print(emp1.generateEmployeeId())