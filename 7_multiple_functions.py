
#simplifying the code
def add(x,y):
    add=x+y # define the mathematics of variables
  #print(add) #print in place of return
    return add
def sub(x,y):
    sub=x-y
  #print(sub)
    return sub

def multi(x,y):
    multi=x*y
 # print(multi)
    return multi

def div(x,y):
    div=x/y  
  #print(div)
    return div

while True:
    operator = input("Enter Operator \n1 for division of Nums \n2 for subtraction of Nums\n3 for Multiplicaiton \n4 for Addition\n")
    if operator in ("1","2","3","4"): # a tuple 
        num1=int(input("Input Number \n"))
        num2=int(input("Input 2nd Number \n"))
    if operator=="1":
        print(div(num1,num2))
    elif operator=="2":
        print(sub(num1,num2))
    elif operator=="3":
        print(multi(num1,num2))
    elif operator=="4":
        print(add(num1,num2))
    Breaking_loop =input("To break loop, Just press enter or any key to show Operator List \n")
    if Breaking_loop =="":
        break

else:
    print("invalid")

