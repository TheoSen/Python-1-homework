#todo list
# creat a class Power that represents an exponent
# the class has instance attribute: exponent: float

class Power:

    def __init__(self, exponent):
        if isinstance(exponent,(int,float)):
            self.exponent = exponent
        else:
            raise TypeError("The exponent must be a numerical value.")
        
    def __call__(self,x):
        if isinstance(x,(int,float)):
            #return x to the power of exponent
            return x ** self.exponent
        else:
            raise TypeError("Input must be a numerical value.")
        
    def __mul__(self,other):
        #  numerical number
        if isinstance(other,(int,float)):
            return Power(other + self.exponent)
        # instance of Power
        elif isinstance(other, Power):
            return Power(other.exponent + self.exponent)
        else:
            raise NotImplemented
class Square(Power):

    def __init__(self):
        super().__init__(2)