from vehicle import Vehicle

class Car(Vehicle):
  
  def __init__(self, model):
    Vehicle.__init__(self)
    self.model = model

car = Car("Audi")
print(car.start_engine())
print(car.model)
print(car.number_of_wheels)