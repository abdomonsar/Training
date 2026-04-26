#Concept
#Inheritance allows a class to inherit properties and methods from another class
#Practice
class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("Some Sound")
    #Cild Class
class Dog(Animal):
        def speak(self):
            print("Woof")    
class  Cat(Animal):
        def speak(self):
            print("Meow")       
dog = Dog("Rex")  
cat = Cat("Luna")  
dog.speak()  
cat.speak()        
 
#Example
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print("General work")

class Developer(Employee):
    def work(self):
        print(f"{self.name} is coding")

class Manager(Employee):
    def work(self):
        print(f"{self.name} is managing team")

e1 = Developer("Ahmed", 8000)
e2 = Manager("Sara", 10000)

e1.work()
e2.work()
