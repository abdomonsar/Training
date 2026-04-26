#Concept
#Methods are functions defined inside a class.
# They describe the behavior of an object.
# Types of methods:
#-Instance Methods → work with object data (self)
#-Class Methods → work with class data (cls)
#-Static Methods → independent (no self or cls)
#practice
class Salary:
    Salary=70000
    def __init__(self,name,increase):
         self.name=name
         self.increase=increase
    #Static Methods
    @staticmethod
    def Salary_data():
         return "Salary data:"      
    @classmethod
    def  Basic_salary(cls) :
         return f"Your basic salary: {cls.Salary}"
    def Salary_with_increase(self):
           return f"Name:{self.name}\n Salary with increase: {self.Salary + self.increase}"
data=Salary("Abdulmajeed",5000)    
print(data.Salary_data())
print(data.Basic_salary())
print(data.Salary_with_increase())

#Example
class BankAccount:
    bank_name="YKB"
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough balance")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}")

    def show_balance(self):
        print(f"Balance: {self.balance}")
    @classmethod
    def Bank_Name(cls): 
         return f"Bank Name:{cls.bank_name}"   
    @staticmethod
    def thanks():
         return "Thank You"


acc = BankAccount("AbdulMajeed", 30000)
print(acc.Bank_Name())
acc.deposit(500)
acc.withdraw(300)
acc.show_balance()
print(acc.thanks())