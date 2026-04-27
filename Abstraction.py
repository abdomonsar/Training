#Concept
# Hiding complex implementation and showing only essential features
#Practice
from abc import ABC, abstractmethod
 
class RemoteControl(ABC):       # Abstraction
    @abstractmethod             #Abstract function
    def turn_on(self):
        pass
class TV(RemoteControl):
    def turn_on(self):
        print("The TV screen is on now...")  
class AC(RemoteControl):
    def turn_on(self):
        print("The air conditioner started to cool the room...")
my_remote=TV()
my_remote.turn_on()                 
#Example
class Delivery(ABC):

    @abstractmethod
    def deliver(self):
        pass

class CarDelivery(Delivery):
    def deliver(self):
        print("Delivering by car")

class DroneDelivery(Delivery):
    def deliver(self):
        print("Delivering by drone")

methods = [CarDelivery(), DroneDelivery()]

for m in methods:
    m.deliver()
