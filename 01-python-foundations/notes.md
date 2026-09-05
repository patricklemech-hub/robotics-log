# Python Notes
to sync the vs code with the github make sure you go the the source code with the shortcut: Ctrl + Shift + G

01. Pseudocode 
Frameline (structure) before coding 
Breaking down the problem before codes exist, helping you organize and follow the logics v
Make complicated programs easier to design

02. we can use built in function by briing it out in the code in the series 
such as: name.strip().title()
meaning that the we want string name remove all whitespace then capitalize the first letter. 
So we can execute multiple built in function by execute it in the series 

3. interactive mode 
execute the code immediately in the Terminal 
by call out only: python
it will show ( >>> ) indicate the interactive mode is activated 

4. Net function
Net function is the techinique that group all the function in one order code that after it finished the 1st function order, it will move to next one in the series 
ex: x = int(input("this is the net function"))
Warning: dont over use it since it could complicate things 

5. When execute the function make sure you asign it with something before use. All function need to be asigned 
ex: z = round(float(z), 2)
we round z value to the second sicfig then asigned it with the z value 

6. Return at the end of function>>
The purpose of ( return ) in the def function is acting as a command report back the work done by that function rather than nothing, without return it look like doing work but that person doesn't report back anything achieved from that work 

return also have 2 way of uses 
a. return followed by value -> meaning function report back that value 
b. return is standalone return -> meaning that function end immediately after condition met, usually standalone return is put in the 2nd order condition function 

7. # import syntax 
meaning that we can import the library or module into our code to use the built in function in that library or module.

8. # random library
random library is a built in library that we can use to generate random number or random value from

9. # statistics library
statistics library is a built in library that we can use to calculate the mean, median, mode

10. # sys 
is a built in library that we can use to access the system specific parameters and functions. It provides functionalities for interacting with the Python interpreter and the underlying operating system. The sys module allows you to manipulate the Python runtime environment, handle command-line arguments, manage input/output streams, and perform various system-level operations.

11. # package 
A package is a collection of modules that are organized in a directory hierarchy. It allows you to group related modules together, making it easier to manage and distribute your code. Packages can contain sub-packages, which are nested packages within the main package. Each package typically has an __init__.py file that serves as an initializer for the package and can contain package-level variables or functions.
 # you can look up the package in the python documentation to see what built in function it has and how to use it. by going to "pypi.org" and search for the package you want to use.

12. # api 
is a set of rules and protocols that allows different software applications to communicate and interact with each other. It defines the methods and data formats that applications can use to request and exchange information. APIs enable developers to access specific functionalities or data from external services, libraries, or platforms without needing to understand the underlying implementation details. They provide a standardized way for applications to interact, making it easier to integrate different systems and build upon existing software components.

13. # JSON (JavaScript Object Notation)
A universal, text-based format used by APIs to send data over the internet.
- It looks and behaves almost identical to Python dictionaries `{key: value}` and lists `[]`.
- `import json` is a built-in library in Python.
- `json.dumps(data, indent=2)`: Formats and pretty-prints JSON data.
- `json.loads(text)`: Converts JSON text into a Python dictionary.