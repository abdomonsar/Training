
try:
     number1=int(input("Enter Number1: "))
     op=input("Enter Op(+,-,%,/): ")
     number2=int(input("Enter Number2: "))
     if op == "+":
        total = number1 + number2
     elif op == "-":
        total = number1 - number2
     elif op == "%":
        total = number1 % number2
     elif op == "/":
        if number2 != 0:
            total = number1 / number2
        else:
            total = "Error Division by zero"
     else:
        total = "Invalid Operator"
    
     print(total)  

except ValueError:
    print("Enter number only")
 


    



