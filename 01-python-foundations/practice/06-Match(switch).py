#asking user name
name = input("what is your name?")

#checking user input

match name:
    case "cake":
        print("This cake is delicious")
    case "fruit":
        print("this is a bananba")
    case "chicken":
        print("this is a chicken")
    case _: # underline is for other cases
        print("I don't know what you meant")