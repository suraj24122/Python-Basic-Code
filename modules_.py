# two types of modules in python
#built-in modules and External modules
import math
#import os
import my_module
#external modules
import requests


#built-in modules
print(math.sqrt(16)) # 4.0
my_module.hello() # Hello from my_module!
r = requests.get('https://www.google.com') # <Response [200]>
print(r.text) # HTML content of the page
