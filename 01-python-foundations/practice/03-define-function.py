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

x,y =value()
answer= multiply(x,y)
print("The multiplier of 2 input values is ",answer)

