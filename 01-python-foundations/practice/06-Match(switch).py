#asking user name
name = input("what are you holding")

#checking user input

match name:
    case "cake" | "banana" |"chicken":
        print("This is food")
    
    case _: # underline is for other cases
        print("This is not food")