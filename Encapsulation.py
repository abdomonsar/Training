#Concept
#Encapsulation means hiding internal data of an object and controlling how it is accessed or modified
#Practice
class Personal_Card:
    def __init__(self,owner,Id):
        self.owner=owner
        self.__Id=Id #Private attribute (Encapsulation)
    #Getter    
    def get_id(self):
        return self.__Id  
    #Setter  
    def show(self):
        print(f"Name:{self.owner}\nID:{self.__Id}")

person=Personal_Card("AbdulMajeed",765767)      
person.show()
print(person.get_id()  )
#Example
class Prodect:
    def __init__(self,name,price):
        self.name=name
        self.__price=price
    def get_price(self):
        return self.__price
    def set_price(self,price):
        if price > 0:
            self.__price=price
            print("Price updated")
        else:
              print("Invalid price")
prodect=Prodect("Labtop",30000) 
print(prodect.get_price())      
prodect.set_price(3500)
prodect.set_price(-100)
print(prodect.get_price())           
        
        