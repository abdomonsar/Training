#Concept
# A Class Method is a method that works with the class itself, not individual objects.
#Defined using: @classmethod
#Takes cls instead of self
#Practice
class Company:
        base_salary = 3000 
        def __init__(self,name):
                self.name=name
        def say_hello(self):  
                print(f"Hello {self.name} Your Salary: {Company.base_salary}")  
                #Class Methods     
        @classmethod
        def change_base_salary(cls,new_amount):
                cls.base_salary=new_amount 
                print(f"The salary has been changed to {cls.base_salary}") 

emp1=Company("Ahmed")    
emp2=Company("Ali")  
emp1.say_hello()  
emp2.say_hello()
Company.change_base_salary(90000)
#Example
class Hotel:
        hotel_name="Abdulmajeed"
        total_booked_rooms=0
        def __init__(self,room_number):
                 self.room_number=room_number
                 self.is_booked = False
        def book_room(self):
                if not self.is_booked:
                    self.is_booked = True
                    Hotel.total_booked_rooms += 1 
                    print(f"Room No {self.room_number} has been booked  ")
                else:
                    print(f"Room No{self.room_number} has already been booked")
                            
        @classmethod
        def change_hotel_name(cls,name_new):
                cls.hotel_name=name_new  
                print("The hotel name has been updated to"+ cls.hotel_name)
        @classmethod          
        def get_report(cls):
                print("Hotel name "+ cls.hotel_name)
                print(f"Total rooms booked: {cls.total_booked_rooms}")
room101 = Hotel(101)
room102 = Hotel(102)
room101.book_room()
room102.book_room()
Hotel.get_report()                             
                         
