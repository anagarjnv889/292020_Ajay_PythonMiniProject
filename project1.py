print("___________________________________\n")
print("Welcome to Python Calculator")
print("___________________________________\n")
# Addition calculation
def addition():
    a=int(input("Enter first number\n"))
    b=int(input("Enter second number\n"))
    print("Sum of",a,"and",b,"is -> ",a+b)
    print("Would you like to continue, then press 1, otherwise press 0")
    n=int(input("Enter your choice 1/0 \n"))
    if n==1:
        take_input()
    elif n==0:
        print("Thank you")
    else:
        print("Enter a valid input")
# Subtraction calculation
def subtraction():
    a=int(input("Enter first number\n"))
    b=int(input("Enter second number\n"))
    print("Difference of",a,"and",b,"is -> ",a-b)
    print("Would you like to continue, then press 1, otherwise press 0")
    n=int(input("Enter your choice 1/0 \n"))
    if n==1:
        take_input()
    elif n==0:
        print("Thank you")
    else:
        print("Enter a valid input")
# Multiplication calculation
def multiplication():
    a=int(input("Enter first number\n"))
    b=int(input("Enter second number\n"))
    print("Multiplication of",a,"and",b,"is -> ",a*b)
    print("Would you like to continue, then press 1, otherwise press 0")
    n=int(input("Enter your choice 1/0 \n"))
    if n==1:
        take_input()
    elif n==0:
        print("Thank you")
    else:
        print("Enter a valid input")
# Division calculation
def division():
    a=int(input("Enter first number\n"))
    b=int(input("Enter second number\n"))
    if b>0:
        print("Division of",a,"and",b,"is ->",a/b)
        print("Would you like to continue, then press 1, otherwise press 0")
        n=int(input("Enter your choice 1/0 \n"))
        if n==1:
            take_input()
        elif n==0:
            print("Thank you")
        else:
            print("Enter a valid input")
    else:
        print("Please enter a valid value of divisor")
    
# Modulus calculation
def modulus():
    a=int(input("Enter first number\n"))
    b=int(input("Enter second number\n"))
    if b>0:
        print("Modulus of",a,"and",b,"is ->",a%b)
        print("Would you like to continue, then press 1, otherwise press 0")
        n=int(input("Enter your choice 1/0 \n"))
        if n==1:
            take_input()
        elif n==0:
            print("Thank you")
        else:
            print("Enter a valid input")
    else:
        print("Please enter a valid value of divisor")

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
        addition()
    elif n==2:
        subtraction()
    elif n==3:
        multiplication
    elif n==4:
        division()
    elif n==5:
        modulus()
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
 