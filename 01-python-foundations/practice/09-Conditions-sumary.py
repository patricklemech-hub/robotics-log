#function to ask user enter the number
#keep asking if n is 0 or negative 
def ask():
    while True:
        num = int (input("what is the number?:"))
        if num >0:
            break
    return num



#funciton to print meow at n time 
def askmeow(n):
    i=0
    for i in range(n):
        i += 1
        print("Meow")
   

askmeow(ask())

