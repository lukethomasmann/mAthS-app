import math
import fractions

def orderFactors(number,order):
    for i in range(33):
        if number % (i+1)**order ==0:
            last=((i+1))
    Mcoef = (number/last**order)
    return int(Mcoef),int(last)

sign = lambda x: ('+','-')[x<0]
class vector:
    def __init__(self, *x):
        if len(x) == 0:
            self.vct = (0,0)
        else:
            self.vct = x


    def mod(self):
        squared = sum(map(lambda x: x**2, self.vct))
        return Root(1,2,squared)

    def __mul__(self,other):
        if isinstance(other,(int,float,Root)):
            return vector(*tuple(map(lambda x: x*other, self.vct)))
        elif isinstance(other,vector):
            return vector(*tuple(map(lambda x,y: x*y,self.vct,other.vct)))

    def __rmul__(self,other):
        self.__mul__(other)

    def __add__(self,other):
        return vector(*tuple(map(lambda x,y: x+y,self.vct,other.vct)))

    def __iadd__(self,other):
        return self.__add__(other)

    def __truediv__(self,other):
        if isinstance(other, (int,float,Root)):
            newVct = tuple(fractions.Fraction(x,other) for x in self.vct)
        for i in newVct:
            if i.denominator == 1:
                i = i.numerator
        return vector(*newVct)

    def __sub__(self,other):
        return vector(*tuple(map(lambda x,y:x-y,self.vct,other.vct)))

    def __isub__(self,other):
        return self.__sub__(other)

    def __len__(self):
        return len(self.vct)

    def __str__(self):
        vct2d = '{}{}i{}{}j'.format(sign(self.vct[0]),abs(self.vct[0]),
                                    sign(self.vct[1]),abs(self.vct[1]),)
        if len(self) == 3:
            vct2d += '{}{}k'.format(sign(self.vct[2]),abs(self.vct[2]))
        return vct2d
class Root:
    #initialising thr root and simplifying it
    def __init__(self,coef,order,number):
        root,orderFactor= orderFactors(number,order)
        self.coef = coef*orderFactor
        self.order = order
        self.number = root
    def checkCompat(self,other):
        return (isinstance(other,Root) and Compat(self.order,other.order,self.number,other.number))
    #defining the output when called as a string
    def __str__(self):
        if (self.number == 1) or (self.coef == 0):
            return str(self.coef)
        else:
            return ('{}\{}/{}'.format(self.coef,
                                      self.order,
                                      self.number))

    def __repr__(self):
        if self.number == 1:
            return self.coef
        elif self.coef == 0:
            return 0
        return self

    def __add__(self,other):
        if self.checkCompat(other):
            return Root(self.coef+other.coef,
                            self.order,
                            self.number)
        else:
            return ('{}+{}'.format(other, R1))

    def __iadd__(self,other):
        if self.checkCompat(other):
            self.coef += other.coef

    #TO COMPLETE
    def __sub__(self , other):
        if self.checkCompat(other):
            return Root(self.coef-other.coef,
                            self.order,
                            self.number,)

    def __isub__(self,other):
        if self.checkCompat(other):
            self.coef -= other.coef

    def __mul__(self,other):
        try:
            if Compat(self.order,other.order,True,True):
                N1 = (self.coef**self.order)*self.number
                N2 = (other.coef**other.order)*other.number
                return Root(1,
                        self.order,
                        N1*N2,)
        except:
            if isinstance(other,int) or isinstance(other,float):
                self.coef *= other
    __rmul__ = __mul__

    def __imul__(self,other):
        self = self*other

    #TO COMPLETE
    def __div__(self,other):
        if isinstance(other,int):
            return Root(Fraction(self.coef,other),self.order,self.number)

    def __rdiv__(self,other):
        if isinstance(other,int):
            newC = (self*self)


try:
    V1 = vector(3,4)
    V2 = vector(6,8)
    print (vector(2,3,-4))
    print((V2/2))
except:
    print(err)
