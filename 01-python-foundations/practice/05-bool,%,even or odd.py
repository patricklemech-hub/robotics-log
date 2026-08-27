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
    

num= int(input("what is the number?:"))

main(num)