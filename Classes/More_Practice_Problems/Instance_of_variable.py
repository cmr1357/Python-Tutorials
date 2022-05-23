class vehicle:
    def __init__(self,name,mileage,capacity):
        
        self.name=name
        self.mileage=mileage
        self.capacity=capacity
        
class bus(vehicle):
    pass

Busbus=bus("Volvo",12,50)

print(isinstance(bus,vehicle))
        