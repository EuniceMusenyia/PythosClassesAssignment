# 2) Create 3 files in the classes directory car.py, fruit.py, and bank.py. 
# Define the following classes in each module respectively. 
# Car
# Fruit
# Account
# Each class should have one class attribute and three instance variables.

class Car:
    wheels = 4

    def __init__(self,color, make, model):
        self.color = color
        self.make = make
        self.model = model

    def start_car(self):
        return (f"The {self.color} {self.make} is starting")
    
    def passengers(self):
        return (f"{self.make} {self.model} is carrying 4")
    
    def car_speed(self):
        return(f"{self.make} {self.model} is moving fast")

        
