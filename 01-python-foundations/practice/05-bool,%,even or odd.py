def main(x):
    if is_even(x):
        print("Even")
    else:
        print("Odd")
    return 

def is_even(x):
    if x %2 ==0:
        return True
    else:
        return False
"""
 different way to write this 
    return True if x%2 == 0 else False 
    
 The most clean is: 
    return (x%2==0) , meaning that if x%2 == 0 it will return true else it false because if x is odd number therefore oddnumber %2 cant be ==0    
"""
    

num= int(input("what is the number?:"))

main(num)