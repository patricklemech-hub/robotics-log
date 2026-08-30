def askname():
    name= input("what is your name?:")
    return name


for _ in range(3):
    print ("your name is", askname())