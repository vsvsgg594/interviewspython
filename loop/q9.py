#Variable definition and assignment
inputn = 3
if inputn > 1:
   # check for factors
   for i in range(2,inputn):
       if (inputn % i) == 0:
           print(inputn,"is not a prime number.")
           print(i,"times",inputn//i,"is",inputn)
           break
   else:
       print(inputn,"is a prime number.")
       
#If the input number is less than or equal to 1, then it is not prime
else:
   print(inputn,"is not a prime number.")