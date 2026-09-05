#Except ValueError : in the way that it will not crash the program if the user inputs a string instead of an integer or something else that no suppose to input.
try: 
    x = int( input("Please enter a number: ")) #This command prompts the user to enter a number. The input is then converted to an integer using the int() function. If the user enters a string or any other non-integer value, a ValueError will be raised.
   
#except if the input is not a number, instead of out put the error value, it will show the message   
except ValueError:
    print("Invalid input. Please enter a valid number.") #This command will print an error message indicating that the input was invalid. It informs the user to enter a valid number instead of a string or any other non-integer value.    
    
print(f"You input is {x}")