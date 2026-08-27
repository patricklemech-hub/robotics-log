#to define a function, we use def as the define funciton to save the function sersve as storage to bring out as needed 
def multiply():
    #ask user to input value x and y 
    x = float(input("what is the x value:"))
    y = float(input("what is the y value:"))
    
    #use the input value to execute the calculation
    z = x*y
    z = round(float(z),2)
    #return the value 
    return z 
    

multiply()

