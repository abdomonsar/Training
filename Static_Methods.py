#Concept
# A Static Method is a method that belongs to the class but does not depend on the class or the object.
#Defined using: @staticmethod
#Does NOT use self or cls
#Practice
class MathTools:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b
print(MathTools.add(5, 3))        
print(MathTools.multiply(4, 2))   
#Example
class Academy:
    academy_name="Abdulmajeed Academy "
    total_students = 0
    def __init__(self,course_name):
           self.coures_name=course_name
    def enroll_student(self,student_name)  :
            print("Hello "+ student_name)
            Academy.total_students+=1
    @classmethod
    def change_academy_name(cls,new_name):
              cls.academy_name=new_name   
              print("New Name "+ cls.academy_name)
    @staticmethod
    def is_work_day(day):
          if day == "Friday":
                print("True") 
          else:
                print("Fals")               
python_course=Academy("Python")
python_course=Academy("C++")
python_course.enroll_student("AbdulMajeed")
Academy.change_academy_name("Ahmed Academy")
print(Academy.is_work_day("Friday"))
 

