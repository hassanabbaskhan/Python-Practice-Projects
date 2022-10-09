#simplifying the code
#define 4 set of funstions

def add(x,y):
    #add=x+y # define the mathematics of variables
    return x+y #print(x+y) will result nothing

def sub(x,y):
    #sub=x-y
    return x-y

def multi(x,y):
    #multi=x*y
    return x*y

def div(x,y):
    #div=x/y  
    return x/y

while True:
    
    operator = input("Enter Operator \n1 for division of Nums \n2 for subtraction of Nums\n3 for Multiplicaiton \n4 for Addition\n")
    if operator in ("1","2","3","4"): # a tuple 
        num1=int(input("Input Number \n"))
        num2=int(input("Input 2nd Number \n"))
    if operator=="1":
        print("The devision will be",div(num1,num2))
    elif operator=="2":
        print("the subtraction will be",sub(num1,num2))
    elif operator=="3":
        print("the mulitplicaiton will be",multi(num1,num2))
    elif operator=="4":
        print("The addition will be",add(num1,num2))
    Breaking_loop =input("To break loop, Just press enter or any key to show Operator List \n")
    if Breaking_loop =="":
        break

else:
    print("invalid")
