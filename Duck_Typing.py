#Concept
# “If it looks like a duck and behaves like a duck, it’s a duck”
#Practice
class Bird:
    def fly(self):
        print("The bird flies with its wings")

class Airplane:
    def fly(self):
        print("The plane flies with engines")

class Whale:
    def swim(self):
        print("The whale is swimming")
def lift_off(entity):
    entity.fly()
b = Bird()
a = Airplane()
w = Whale()
lift_off(b)  
lift_off(a)    
# lift_off(w) Error     

#Example
class TextFile:
    def read(self):
        print("Reading text file")

class ImageFile:
    def read(self):
        print("Reading image file")

class VideoFile:
    def read(self):
        print("Reading video file")

files = [TextFile(), ImageFile(), VideoFile()]

for f in files:
    f.read()
