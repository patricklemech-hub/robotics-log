def getin():
    while True:
        try: 
            x = int(input("Please enter a number: "))  # Prompt the user to enter a number and convert it to an integer
            break  # Exit the loop if the input is valid
        except ValueError:
            print("Invalid input. Please enter a valid number.")  # Print an error message if the input is not a valid integer
    return x  # Return the valid input number        
def main():
    x = getin()
    print(f'You input is {x}')  # Print the valid input number
    
main()  # Call the main function to execute the program25
