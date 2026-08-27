#to define a function, we use def as the define funciton to save the function sersve as storage to bring out as needed 
#function that receive input value 
def value():
    x = input("what is the value of x:")
    y = input("what is the value of y:")
    return int(x), int(y)


#function that do calculation 
def multiply(a,b):
    a*b
    return a*b
#Assigned the output of function to variable for calculation function
x,y =value()   # function value output 2 varibles but it hasnt assigned to any. Therefore, we need to assign it to something 

#use assigned variables as input into the calculation function 
answer= multiply(x,y) # use asigned variable to input into the calculation function 
print("The multiplier of 2 input values is ",answer)

