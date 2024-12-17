class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

if __name__ == "__main__":
    cal = Calculator()
    print(cal.add(1, 2))
    print(cal.subtract(3, 2))