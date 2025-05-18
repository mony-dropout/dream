import math
class cc:
    def __init__ (self,x,y):
        self.r=x
        self.i=y
        
    def mag(self):
        return math.sqrt(self.r**2+self.i**2)
    def add(self,c):
        return cc(self.r+c.r,self.i+c.i)
    def smul(self,l):
        return cc(self.r*l,self.i*l)
    def sub(self,c):
        self.add(c.smul(-1))
    
    