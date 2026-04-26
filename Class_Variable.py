#Concept
# A Class Variable is a variable that is shared among all instances of a class.
#Practice
class wallet:
     
    wallet_name="BankLite" # Class Variable
    def __init__(self,name,phone):
         self.name=name
         self.phone=phone
    def show(self):
         print(f"wallet name:{wallet.wallet_name}\nName:{self.name}\nPhone:{self.phone}") 
Wallet_name=wallet("AbdulMajeed",777653902)   
Wallet_name.show()          
#Example
class User:
     User_Count=0
     def __init__(self,name):
          self.name=name
          User.User_Count+=1
user1=User("Ahmed")  
user2=User("Ali")    
user3=User("AbdulMajeed")    
print(User.User_Count)



          

