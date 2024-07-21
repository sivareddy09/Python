from Person import Person
from random import randint
class Employee(Person):

    def __init__(self, firstName, lastName, gender, age) -> None:
        super().__init__(firstName, lastName, gender, age)
        self.__id = self.generateEmployeeId()

    def display(self):
        return f"{super().display()}, EmployeeId: {self.__id}"
    
    def generateEmployeeId(self):
        if len(self.firstName) <= 3 and len(self.lastName) <= 3:
            return f"{self.firstName[0:]+self.generateX(4-len(self.firstName))+self.lastName[0:]+self.generateX(4-len(self.lastName))+str(randint(0, 1000))}"
        return f"{self.firstName[:4]+self.lastName[:4]+str(randint(0, 1000))}"

    def generateX(self, value):
        return 'X'*value
    
if __name__ == '__main__':
    emp = Employee("SivaPrasadReddy", "Geddam", "Male", 25)
    print(emp.display())
    # print(emp.generateEmployeeId())
    
    emp1 = Employee("Siv", "Ged", "Male", 25)
    print(emp1.display())
    # print(emp1.generateEmployeeId())