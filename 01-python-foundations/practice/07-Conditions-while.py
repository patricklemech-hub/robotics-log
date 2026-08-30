def askname():
    name=input("what is your name?:")
    return name

while True: #true means the loop will run until the break statement is executed, since Ture is always true the loop will run until the break statement is executed therefore it will run infinitely until the break statement is executed
    #ask for the number 
    number=input("what is your number?:")

    #checking the correct number  
    if number in [ "1","2","3"]:                    #meaning if guessing number is in range of 1 to 3 the loop will break and print the message
        print ("Your number in the winning range")
        break
    else: #if the number is not in the range of 1 to 3 then it will print the message and ask for the number again
        print("Your number is not correct, please try again")
       