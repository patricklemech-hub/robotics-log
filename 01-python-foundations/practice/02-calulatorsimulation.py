

x = input("Input value of X:")
y = input("Input value of Y:")
z = float(x) + float(y) # the reason why we have to put input values x and y in term of interger because, the orginal form of input is the string therefore we need to define it as interger for calculation
z= round(float(z),2)

print("Sum of value X and Y is:","", z)  