# TryHackMe Room: "Scripting"  

## Task 1: Base64 - Easy  

"This file has been base64 encoded 50 times - write a script to retrieve the flag. Here is the general process to do this:

- read input from the file
- use function to decode the file
- do process in a loop  
Try do this in both Bash and Python!"  

## Task 1: My Solution  
[Python Script](https://github.com/CheeseC4k3/TryHackMe-Scripting/blob/main/thmbase.py)  

## Task 2: Gotta Catch em All - Medium

"You need to write a script that connects to this webserver on the correct port, do an operation on a number and then move onto the next port. Start your original number at 0.

The format is: operation, number, next port.

For example the website might display, add 900 3212 which would be: add 900 and move onto port 3212.

Then if it was minus 212 3499, you'd minus 212 (from the previous number which was 900) and move onto the next port 3499

Do this until you the page response is STOP (or you hit port 9765).

Each port is also only live for 4 seconds. After that it goes to the next port. You might have to wait until port 1337 becomes live again...

Go to: http://<machines_ip>:3010 to start..."  


## Task 2: My Solution  
[Python Script](https://github.com/CheeseC4k3/TryHackMe-Scripting/blob/main/thmsocket.py)  

## Task 3: Encrypted Server Chit Chat - Hard
"The VM you have to connect to has a UDP server running on port 4000. Once connected to this UDP server, send a UDP message with the payload "hello" to receive more information. You will find some sort of encryption(using the AES-GCM cipher). Using the information from the server, write a script to retrieve the flag. Here are some useful thingsto keep in mind:

sending and receiving data over a network is done in bytes
the PyCA encryption library and functions takes its inputs as bytes
AES GCM sends both encrypted plaintext and tag, and the server sends these values sequentially in the form of the encrypted plaintext followed by the tag
This machine may take up to 5 minutes to configure once deployed. Please be patient. 

Use this general approach(use Python3 here as well):

Use the Python sockets library to create a UDP socket and send the aforementioned packets to the server
use the PyCA encyption library and follow the instructions from the server"  

## Task 3: No Solution available yet  