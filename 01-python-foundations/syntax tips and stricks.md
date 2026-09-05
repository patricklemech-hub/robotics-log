#comment
to leave a comment we use ( # ) 
if we want to leave multiple lines of comment we could go down with ( # ) 
However if we dont want to repeat the # we can use ( """ ) at the begining of the list of comment then end with ( """ ) 

#syntax
1. string str 
2. integer int 
3. Boolian 

#print
1. end="\n" # \n in here meaning that at the end it will go to the new line 
if we write end="" empty there for it wont go to the new line instead it will keep going. Therefore, end="" is use for define the comand at the end 
2. sep="" same idea as end="" but for spacing, depend on what we want to put in the spacing, it could be a ? or something else that we want to input 
3. fomat string or f string 
such as: print(f"this is a fomat string {variables}")
we use {} do determine the variable when use f string 
4. .strip() 
remove whitespace from string input 
ex: name = name.strip()

5. .split(center of split point)
use to split the variable from the split point 
such as: name =Patrick LE 
name.split() output are 2 varible first haft and second haft seperated by empty space () 

##integer
int 
+ - * / % 

##float 
float number with decimal number 
4.2 4.5 etc..

##return in the function structure
return sends a value back from a function so you can use it somewhere else in your program.
print()vs return ,
print() is send out hte result 
return is use the result for next step 

6. Conditional 
comparation
>, <, <= , >=, == : equal, != 

7. # Modulo operator 
giving remainder after devided 
2 / 2 = 1.0 , 0 is the remainder 
% purpose is the sort out the remainder 

8. # Match or (switch) 
Match input :
    case "input match": 
        condition

9. # Bitwise for Match case 
"|" in case fucntion of Match we can't use or since it doesnt work out. 

10. # While and for 
while loop is use for infinity condition
for loop is use for condition 

11. # list in python
"in" " [a,c,b,c] " 

12. # funtion range(number of range):
use for range 

13. # Exception Handling: Used to catch errors and prevent program crashes.
Rule: A 'try' block must always be paired with an 'except' (or 'finally').
try: Code that might fail | except: Runs if an error happens | else: Runs if no error | finally: Always runs.

14. # pass statement
`pass` is a placeholder that does nothing. It is used when Python requires code (like in an `if`, `loop`, `function`, or `except`), but you want to ignore it or write it later without causing a syntax error.

15. # raise statement
`raise` is used to manually trigger (throw) an error when a specific condition occurs.
Example: 
if age < 0:
    raise ValueError("Age cannot be negative")

16. # random module
Use `import random` to generate random numbers or pick random items.
- `random.choice(list)`: Picks one random item from a list.
- `random.randint(a, b)`: Returns a random integer between a and b (inclusive).
- `random.shuffle(list)`: Mixes/shuffles a list in place.
- `random.random()`: Returns a random float between 0.0 and 1.0.
