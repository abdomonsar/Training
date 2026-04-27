#Concept
# Composition is a relationship where:
# One object contains another object and fully controls its lifecycle
#Practice
class Engine:
    def __init__(self):
        self.power = 100

class Car:
    def __init__(self):
        self.engine = Engine()  # Composition

    def show(self):
        print(f"Engine Power: {self.engine.power}")

c = Car()
c.show()
#Example
class CPU:
    def process(self):
        print("Processing...")

class Computer:
    def __init__(self):
        self.cpu = CPU()  # Composition

    def run(self):
        self.cpu.process()

pc = Computer()
pc.run()