#Concept
# Instance Variables are variables that belong to each object separately.
#Practice
class Motorcycle:
    def __init__(self,brand,speed):
         # Instance Variable
        self.brand=brand
        self.speed=speed
motorcycle1=Motorcycle("Toyota",120)
motorcycle2=Motorcycle("KTM",130)
print(motorcycle1.brand)
print(motorcycle2.brand)

#Example
class Device:
    def __init__(self, name):
        self.name = name
        self.battery = 100    
        self.temperature = 25

    def use(self):
        self.battery -= 10
        self.temperature += 5

d1 = Device("Phone")
d2 = Device("Laptop")

d1.use()

print(d1.battery)   
print(d2.battery)   