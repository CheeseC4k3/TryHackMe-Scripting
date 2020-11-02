from base64 import *

file = open("b64.txt", "r")
file = file.read()
code = file
for i in range (0,50):
    code = b64decode(code)
print(code)