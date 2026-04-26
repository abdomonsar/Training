#Concept
#A constructor in Python is a special method called automatically when an object is created
#Practice
class Student:
    # constructoes(__init__)
    def __init__(self,name,age):
         # Initialization 
         self.name=name
         self.age=age
    def Show(self):
         print(f"Name:{self.name} \nAge:{self.age}")     

student=Student("AbdulMajeed",34)         
student.Show()
#Example
class Phone:
     def __init__(self,model,storege,price):
          self.model=model
          self.storege=storege
          self.price=price
     def info(self):
          print(f"model:{self.model}\nstorege{self.storege}\nprice:{self.price}")  
phone=Phone("iPhone 14",125,1000)   
phone.info()                
          
