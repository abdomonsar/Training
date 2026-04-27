#Concept
# Association is a relationship between two classes where objects know about each other.
#Practice
class Driver:
    def __init__(self, name):
        self.name = name

    def drive(self, car):
        print(f"{self.name} is driving {car.model}")

class Car:
    def __init__(self, model):
        self.model = model


d = Driver("Ahmed")
c = Car("Toyota")

#Association
d.drive(c)
#Example
class Course:
    def __init__(self, title):
        self.title = title

class Teacher:
    def __init__(self, name):
        self.name = name

    def teach(self, course):
        print(f"{self.name} is teaching {course.title}")

t = Teacher("Sara")
c = Course("Math")

t.teach(c)