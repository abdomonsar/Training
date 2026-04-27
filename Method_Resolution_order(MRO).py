#Concept
# MRO (Method Resolution Order) defines the order in which Python searches for methods and attributes in a class hierarchy.
#Practice
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

d = D()
d.show()
#Example
class Base:
    def process(self):
        print("Base")

class Security(Base):
    def process(self):
        print("Security Check")

class Logging(Base):
    def process(self):
        print("Logging")

class System(Security, Logging):
    pass

s = System()
s.process()
print(System.__mro__)
