#dictionary and list in a same command 

students = [
    {"name": "John", "age": 20, "major": "Computer Science"},
    {"name": "Alice", "age": 22, "major": "Mathematics"},
    {"name": "Bob", "age": 21, "major": "Physics"}, 
    {"name": "Diana", "age": 23, "major": "Biology"},
    
]
for student in students:
    print(student["name"], student["age"], student["major"], sep="|") #This command will print the name, age, and major of each student in the list. The sep parameter is used to separate the values with "->". For example, John is 20 years old and majors in Computer Science, Alice is 22 years old and majors in Mathematics, and so on.