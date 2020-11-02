# TryHackMe Room: "Scripting"  

## Task 1: Base64 - Easy  

"This file has been base64 encoded 50 times - write a script to retrieve the flag. Here is the general process to do this:

read input from the file
use function to decode the file
do process in a loop
Try do this in both Bash and Python!"  

## Task 2: Gotta Catch em All - Medium

"You need to write a script that connects to this webserver on the correct port, do an operation on a number and then move onto the next port. Start your original number at 0.

The format is: operation, number, next port.

For example the website might display, add 900 3212 which would be: add 900 and move onto port 3212.

Then if it was minus 212 3499, you'd minus 212 (from the previous number which was 900) and move onto the next port 3499

Do this until you the page response is STOP (or you hit port 9765).

Each port is also only live for 4 seconds. After that it goes to the next port. You might have to wait until port 1337 becomes live again...

Go to: http://<machines_ip>:3010 to start..."  

## Task 1: My Solution:  
[Python Script](https://github.com/CheeseC4k3/TryHackMe-Scripting/blob/main/thmbase.py)  
## Task 2: My Solution:  
[Python Script](https://github.com/CheeseC4k3/TryHackMe-Scripting/blob/main/thmsocket.py)  
## Task 3: not available