import matplotlib.pyplot as plt
%matplotlib inline
class circle(object):
    def __init__(self, color, radius):
        self.color = color
        self.radius = radius 

    def drawCircle(self):
        print("Print")
        
class Car(object):
    def __init__(self, make, model, color, owner_number):
        self.make = make
        self.model = model
        self.color = color
        self.owner_number = owner_number 
    def car_info(self):
        print("make: ",self.make)
        print("model:", self.model)
        print("color:",self.color)
        print("number of owners:",self.owner_number)
    def sell(self):
        self.owner_number = self.owner_number+1

