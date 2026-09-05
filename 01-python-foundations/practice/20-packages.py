#package is a collection of modules that are organized together in a directory hierarchy. It allows you to group related modules and provide a way to distribute and share code. Packages can contain sub-packages, modules, and other resources, making it easier to manage and organize larger codebases. By using packages, you can create reusable components, promote code modularity, and facilitate collaboration among developers.

import cowsay 
import sys
 
if len(sys.argv) == 2: #This command uses the cowsay module to display a message in the form of a speech bubble with an ASCII art representation of a cow. The cowsay.cow() function takes a string argument, which is the message to be displayed. In this case, it will print "Hello, I'm a cow!" along with the cow ASCII art.
    cowsay.cow("hello, " + sys.argv[1]) #This command uses the cowsay module to display a message in the form of a speech bubble with an ASCII art representation of a cow. The cowsay.cow() function takes a string argument, which is the message to be displayed. In this case, it will print "Hello, I'm a cow!" along with the cow ASCII art.
    