#dictionary Dict is a data structure that stores data in key-value pairs. Each key is unique and maps to a specific value. Dictionaries are mutable, meaning you can change their contents after creation.
#something pair with something 
#syntax: dict = {key1: value1, key2: value2, key3: value3}

student = {
    "mango": "fruit",
    "carrot": "vegetable",
    "banana": "fruit",
    "broccoli": "vegetable",
}

def nameprint():
    for name in student:
         return print(name, student[name], sep="->") #This command will print the key-value pairs in the dictionary. The key is the name of the item, and the value is the type of item (fruit or vegetable). For example, mango is a fruit, carrot is a vegetable, and so on
        #we also modified the spacing fromm blank space to "->" using the sep parameter in the print function. The sep parameter specifies the string that is inserted between the items to be printed. In this case, we used "->" to separate the key and value in the output.

def test():
    for test in student: 
        return print(test) #This command will print the key-value pairs in the dictionary. The key is the name of the item, and the value is the type of item (fruit or vegetable). For example, mango is a fruit, carrot is a vegetable, and so on
    
if print(student["Mana"]) is False:
    print("Mana is not in the dictionary") #This command will print a message indicating that "Mana" is not a key in the dictionary. Since "Mana" is not present in the dictionary, the output will be "Mana is not in the dictionary".