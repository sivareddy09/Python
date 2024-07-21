
class ConvertTemparatures:
    def __init__(self, *args):
        self.args = list(args)
        
    def convertCelsiusToFarenheit(self):
        data = []
        for i in self.args:
            fh = (i*9/5)+32
            data.append(fh)
        return data
        
    def convertFarenheitToCelsius(self):
        data = []
        for i in self.args:
            cel = (i-32)*5/9
            data.append(round(cel,1))
        return data
            

if __name__ == '__main__':
    c = ConvertTemparatures(23, 24, 25, 26)
    print(f"Celcius to Farenheit: {c.args} : {c.convertCelsiusToFarenheit()}")

    c1 = ConvertTemparatures(73.4, 74.4, 75.4, 76.4)
    print(f"Farenheit to Celcius: {c1.args} : {c1.convertFarenheitToCelsius()}")