# Define the local and Global variables with the same name and print both variables and 
# understand the scope of the variables
c=10
def add(a,b):
    print(a,b)# a and b is local
    print(c)
add(20,30)    
