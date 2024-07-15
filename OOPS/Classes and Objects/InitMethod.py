
class Calculation:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a+self.b
    
    def sub(self):
        return self.a-self.b
    

if __name__ == '__main__':
    cal = Calculation(2, 4)
    print(cal.add())
    print(cal.sub())