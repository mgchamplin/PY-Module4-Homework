class Currency:

    currencies =  {'CHF': 0.930023, #swiss franc 
                 'CAD': 1.264553, #canadian dollar
                 'GBP': 0.737414, #british pound
                 'JPY': 111.019919, #japanese yen
                 'EUR': 0.862361, #euro
                 'USD': 1.0} #us dollar
      
    def __init__(self, value, unit="USD"):
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{round(self.value,2)} {self.unit}"

    def __repr__(self):
        return f"{round(self.value,2)} {self.unit}"

    def changeTo(self, new_unit):
        
        self.value = (self.value / Currency.currencies[self.unit] * Currency.currencies[new_unit])
        self.unit = new_unit 
    #
    # Operations - Add and variations
    #
    def __add__(self,other):
        if type(other) == int or type(other) == float:      # if it is a int or float, then mult and we're done
            val = (other * Currency.currencies[self.unit])
        else:                                               # Adjust for currency rate
            val = (other.value / Currency.currencies[other.unit] * Currency.currencies[self.unit]) 
        return (Currency(val + self.value, self.unit))

    def __iadd__(self, other):
        return Currency.__add__(self,other)

    def __radd__(self, other):
        result = self + other
        if self.unit != "USD":
            result.changeTo("USD")
        return result
    #
    # Operations - Subtract and variations
    #
    def __sub__(self,other):
        if type(other) == int or type(other) == float:      # if it is a int or float, then mult and we're done
            val = (other * Currency.currencies[self.unit])
        else:                                               # Adjust for currency rate
            val = (other.value / Currency.currencies[other.unit] * Currency.currencies[self.unit]) 
        return (Currency(self.value - val, self.unit))

    def __isub__(self, other):
        return Currency.__sub__(self,other)

    def __rsub__(self, other):
        result = other - self.value
        result = Currency(result,self.unit)
        if self.unit != "USD":
            result.changeTo("USD")
        return result
    #
    # Operations - Multiply 
    #
    

#============== FOR HOMEWORK VERIFICATION
v1 = Currency(23.43, "EUR")
v2 = Currency(19.97, "USD")
print("v1 = ", v1, " v2 = ", v2)

print(v1 + v2)
print(v2 + v1)
print(v1 + 3) # an int or a float is considered to be a USD value
print(3 + v1)
print(v1 - 3) # an int or a float is considered to be a USD value
print(30 - v2) 
print("==================")


v3 = Currency(12.50, "USD")
v4 = Currency(17.50, "USD")
print(v3 + v4)

