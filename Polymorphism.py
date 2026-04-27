#Concept
#Same method name, different behavior
#Practice
class Shape:
    def area(self):
        pass
class Square(Shape):
    def __init__(self,side):
        self.side=side
        # Polymorphism
    def area(self):
        return    self.side * self.side 
class Circle(Shape)  :
    def __init__(self,radius):
         self.radius=radius
        #  Polymorphism
    def area(self):
        return 3.14 *(self.radius ** 2)
shapes = [Square(10), Circle(5)]    
for shape in shapes:
    print(f"Space is: {shape.area()}")
#Example
class Payment:
    def pay(self,amount):
        print("Processing payment")
class CreditCard(Payment)  :
    def pay(self,amount)   :
        print(f"Paid {amount} using Credit Card") 
class PayPal(Payment) :
    def pay(self ,amount) :
        print(f"Paid {amount} using PayPal") 
class ApplePay(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Apple Pay")  
methods = [CreditCard(), PayPal(), ApplePay()]
for m in methods:
   m.pay(100)                