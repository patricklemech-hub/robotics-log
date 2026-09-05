import requests
import sys
import json 

if len(sys.argv) != 2: #This command checks if the length of the command-line arguments passed to the script is equal to 2. It ensures that the user has provided a URL as an argument when running the script. If the condition is true, it proceeds to make an HTTP GET request to the specified URL.
    sys.exit()
    
    
response = requests.get(sys.argv[1]).

