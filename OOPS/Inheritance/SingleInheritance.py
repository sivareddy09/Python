
class Person:

    def __init__(self, name, age, gender, email, phoneNumber, address) -> None:
        self.name = name
        self.age = age
        self.gender = gender
        self.email = email
        self.phoneNumber = phoneNumber
        self.address = address

    def getDetails(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Email: {self.email}, Phone Number: {self.phoneNumber}, Address: {self.address}"
    

class Employee(Person):

    def __init__(self, name, empId, age, gender, email, phoneNumber, address):
        super().__init__(name, age, gender, email, phoneNumber, address)
        self.empId = empId

    def getDetails(self):
        return f"EmpId: {self.empId}, {super().getDetails()}"

if __name__ == '__main__':
    person = Person("Siva", 25, "Male", "gspr991@gmail.com", 9640718354, "Rajampet")
    print(person.getDetails())

    employee = Employee("Siva", 439, 25, "Male", "gspr991@gmail.com", 9640718354, "Rajampet")
    print(employee.getDetails())