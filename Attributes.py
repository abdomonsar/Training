#Concept
#Attributes are variables that belong to a class or an object.
# They store the data (state) of an object.
#There are two main types:
#-Instance Attributes
#-Class Attributes
#Practice
class Car :
    #Class Attributes
    wheels=4
    def __init__(self,brand,color):
        #Instance Attributes
        self.brand=brand
        self.color=color
         
car1=Car("Toyota","Red")
car2=Car("BMW", "Black")
#Example
class User:
    Platform_Name="Smart Mind"
    def __init__(self,user_name,email):
         self.user_name=user_name
         self.email=email
user1=User("AbdulMajeed","abdo@gmail.com") 
user2=User("Ahmed","Ahmed@gmail.com")   
print(user1.Platform_Name)    
print(user2.Platform_Name) 
print(user1.user_name)