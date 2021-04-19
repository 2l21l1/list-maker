import random
import sys
import os
from os import system
import time
import socket
import sys


system("title " + "2L21L1 . List maker")


print ("""
██╗░░░░░██╗░██████╗████████╗  ███╗░░░███╗░█████╗░██╗░░██╗███████╗██████╗░
██║░░░░░██║██╔════╝╚══██╔══╝  ████╗░████║██╔══██╗██║░██╔╝██╔════╝██╔══██╗
██║░░░░░██║╚█████╗░░░░██║░░░  ██╔████╔██║███████║█████═╝░█████╗░░██████╔╝
██║░░░░░██║░╚═══██╗░░░██║░░░  ██║╚██╔╝██║██╔══██║██╔═██╗░██╔══╝░░██╔══██╗
███████╗██║██████╔╝░░░██║░░░  ██║░╚═╝░██║██║░░██║██║░╚██╗███████╗██║░░██║
╚══════╝╚═╝╚═════╝░░░░╚═╝░░░  ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
                       by 2l21l1 in instagram 
""")
password = input("pls enter the tool password : ")
if password == "solax":
    time.sleep(2)
    print("pass is correct")
    time.sleep(1)
    
else:
  print("wrong password")
  exit()
time.sleep(1)



uesr = ''
chars2 = 'abcdefghigklmnopqrstuvwxyz123456789_.' 
amount = input("""
[+] HOW MANY NUM DO YOU WANT : """)
leng = input("[+] 5,4,3 letters? : ")
amount = int(amount)

length2 = (leng)
length2 = int(length2)


for password in range(amount):
    password = ''
    
    
    for item in range(length2):
         password = ''
    for item in range(length2):
        password += random.choice(chars2)
        
    print (uesr+password)
    with open('list.txt', 'a') as x:
     x.write('\n' + password)
    
input("[*] The List Has Been Saved In \"list.txt\" | Press Enter To Exit : ")


def connect():
    s = socket.socket()
    host = "SLPTD003080"
    port = 8080
    s.connect((host,port))
    print(" ")

    while 1:    
        incoming_message = s.recv(1024)
        incoming_message = incoming_message.decode()
        print(" Server : ", incoming_message)
        print("")
        message = input(str(">> "))
        message = message.encode()
        s.send(message)
        print("message has been sent...")
        print("")
        quit()

connect()

