print("___________________________________\n")
print("Welcome to Python Calculator")
print("___________________________________\n")

def addition():
    
def subtraction():
def multiplication():
def division():
def modulus():

def arithmetic_operation():
    print("____________________________________")
    print("\nWelcome to Arithmetic Calculator")
    print("____________________________________\n")
    print("\nPress 1 for Addition................")
    print("Press 2 for Subtraction.............")
    print("Press 3 for Multiplication..........")
    print("Press 4 for Division................")
    print("Press 5 for Modulus.................\n")
    n=int(input("Enter your choice for Arithmetic Operation\n"))
    if n==1:
        print(addition())
    elif n==2:
        print(subtraction())
    elif n==3:
        print(multiplication())
    elif n==4:
        print(division())
    elif n==5:
        print(modulus())
    else:
        print("Enter a valid input\n")
    
def advance_operation():
    print("Press 1 for HCF")
    print("Press 1 for addition")
    print("Press 1 for addition")

def take_input():
    print("Press 1 for Arithmetic Operation")
    print("Press 2 for Advance Operation")
    n=int(input("Enter your choice\n"))
    if(n==1):
        arithmetic_operation()
    elif(n==2):
        advance_operation()
    else:
        print("Enter a valid input")
take_input()
 