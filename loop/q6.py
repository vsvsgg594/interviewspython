# Write a program to print largest number among three numbers.

num1=int(input("enter the number :"))
num2=int(input("enter the number :"))
num3=int(input("enter the number : "))
if(num1>num2):
    if(num1>num3):
        print(num1+"is largest number ")
elif  num2>num1:
    if num2>num3:
        print(num2+"is largest number ")
else:
    print(num3+"is largest number ")        
         
