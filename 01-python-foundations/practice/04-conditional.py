#condition if else elseif 
#or 

#ask user to input 
x = float(input("what is the value of x?:"))
y = float(input("what is the value of y?:"))
score = float(input("what is your score?:"))

#checking function
def checking(x,y):
    if x == y: 
        print("x and y is equal to each other!")
    elif x>y:
        print("x is larger than y")
    else:
        print("x is smaller than y")

#checking
def scorechecking(x):
    #checking range
    if x<=850 and x >=300:
     
        if x>=740:
            print("Your score is poor score! keep it up!")
        
        elif x>=670:
                print("Your score is fair score! keep it up!")
        
        elif x>=580 :
                print("Your score is good score! keep it up!")
        
        elif x>=300:
                    print("Your score is really good score! keep it up!")
            
    else:
        print("sorry your input is out of range")

scorechecking(score)



