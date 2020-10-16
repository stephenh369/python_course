from vehicle import *

class Motorbike(Vehicle):

  def __init__(self):
    self.number_of_wheels = 2

  def start_engine(self):
    return "Vroom, I'm a bike!"

bike = Motorbike()
print(bike.start_engine())