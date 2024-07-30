# Write a function for arithmetic operators(+,-,*,/)

def arithmeticfun():
    num1=int(input("enter the number :"))
    num2=int(input("enter the second number "))
    add=num1+num2
    print("add "+add)
    if num1>num2:
        sub=num1-num2
        print("subtract "+sub)
    else:
        sub=num2-num1
        print(sub)
    mul=num1*num2
    print("multiplication "+mul)    
    div=num1/num2
    print("division "+div) 

arithmeticfun()

