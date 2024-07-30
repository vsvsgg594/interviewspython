#  Program for relational operators (<,<==, >, >==)

num1=int(input("enter the number :"))
num2=int(input("enter the number :"))
if num1<num2:
    print(num2+" is greater than"+num1)
elif num1>num2:
    print(num1+"is greater  than "+num2) 
elif num1>=num2:
    print(num1+"is greater than or equal to "+num2) 
else:
    print(num2+"is greater than or equal to "+num1)        
