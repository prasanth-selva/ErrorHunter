 
'''
Create a menu to perform basic mathematical operations (addition, subtraction, multiplication, division, modulo) on two numbers.

'''
 
def math_operations_menu(a,b,operator):
   
 
def math_operations_menu():
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulo")
    
    choice = int(input("Enter your choice: "))
 

    a, b = map(int, input("Enter two numbers: ").split(sep=","))

 
 
 
    a=int(input("enter a number1:"))
    b=int(input("enter a number2:"))
 
 
    if choice == 2:
        print("Subtraction:", a - b)   
    elif choice == 1:
        print("Addition:", a + b)   
    elif choice == 4:
 
        print("Division:", a / b)   
 
        print("Division:", a / b)   
 
        if b==0:
            print("zero error")
        else:
            print("Division:", a / b)   
 
 
    elif choice == 3:
        print("Multiplication:", a * b)   
    elif choice == 5:
        print("Modulo:", a // b)   
    else:
        print("Invalid option")
 
print("1. Addition")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulo")
choice = int(input("Enter your choice: "))
num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
math_operations_menu(num1,num2,choice)
 
 
 
 
    a, b = map(int , input("Enter two numbers: ").split())

    if choice == 1:
        print("addition:", a + b)
    elif choice == 2:
        print("subtraction:", a - b)   
    elif choice == 3:
        print("multiply:", a * b)   
    elif choice == 4:
        print("divide:", a / b)   
 
 