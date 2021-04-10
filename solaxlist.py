import random
import sys
import os
from os import system
import time

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
    print("pass is correct")
    time.sleep(1)
else:
  print("wrong password")
  exit()
time.sleep(1)
print ("""
────────╔╗──────────────╔╗─────╔╗╔╗──────╔╗──────╔╗
────────║║─────────────╔╝╚╗───╔╝╚╣║─────╔╝╚╗─────║║
╔╗╔╗╔╦══╣║╔══╦══╦╗╔╦══╗╚╗╔╬══╗╚╗╔╣╚═╦══╗╚╗╔╬══╦══╣║
║╚╝╚╝║║═╣║║╔═╣╔╗║╚╝║║═╣─║║║╔╗║─║║║╔╗║║═╣─║║║╔╗║╔╗║║
╚╗╔╗╔╣║═╣╚╣╚═╣╚╝║║║║║═╣─║╚╣╚╝║─║╚╣║║║║═╣─║╚╣╚╝║╚╝║╚╗
─╚╝╚╝╚══╩═╩══╩══╩╩╩╩══╝─╚═╩══╝─╚═╩╝╚╩══╝─╚═╩══╩══╩═╝ """)
time.sleep(1)
print ("")
time.sleep (1)
print ("""
█▀ ▀█▀ ▄▀█ █▀█ ▀█▀ █ █▄░█ █▀▀   ▀█▀ █▀█ █▀█ █░░   █▀ ▀█
▄█ ░█░ █▀█ █▀▄ ░█░ █ █░▀█ █▄█   ░█░ █▄█ █▄█ █▄▄   █▄ ▄█""")
time.sleep (2)




uesr = ''
chars2 = 'abcdefghigklmnopqrstuvwxyz123456789_.' 
amount = input("""
how many numbers do you want [+]:""")
amount = int(amount)

length2 = ('4')
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

