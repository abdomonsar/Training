#Concept
# Aggregation is a type of association where:
# One object contains another object, but both can exist independentl
#Practice
class Employee:
    def __init__(self, name):
        self.name = name

class Company:
    def __init__(self, employees):
        self.employees = employees  # Aggregation

    def show_employees(self):
        for emp in self.employees:
            print(emp.name)


e1 = Employee("Ahmed")
e2 = Employee("Sara")
c = Company([e1, e2])
c.show_employees()
#Example
class Song:
    def __init__(self, title):
        self.title = title

class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def play(self):
        for song in self.songs:
            print(f"Playing {song.title}")

s1 = Song("Song 1")
s2 = Song("Song 2")

pl = Playlist([s1, s2])

pl.play()