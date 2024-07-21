
class Person:

    def __init__(self, firstName, lastName, gender, age) -> None:
        self.firstName = firstName
        self.lastName = lastName
        self.gender = gender
        self.age = age

    def display(self):
        return f"FirstName: {self.firstName}, LastName: {self.lastName},Gender: {self.gender}, Age: {self.age}"