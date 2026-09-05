# system 

import sys #This command imports the sys module, which provides access to system-specific parameters and functions in Python. The sys module allows you to interact with the Python interpreter and perform various operations related to the system environment, such as accessing command-line arguments, manipulating the Python path, and handling standard input/output streams.


print("hello, my name is ", sys.argv[0]) #This command prints a message to the console that includes the name of the script being executed. The sys.argv list contains the command-line arguments passed to the script, and sys.argv[0] specifically refers to the name of the script itself. In this case, it will print "hello, my name is" followed by the name of the script file.