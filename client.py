
#----- A simple TCP client program in Python using send() function -----

import socket
import  os

def inp():
    val1 = input("Enter first Number :")
    val2 = input("Enter Second Number :")
    return str(val1)+','+str(val2)+','



print("Enter Server Details\n")
serverIP =  input("Enter Server IP : ")
os.system('cls')

 

# Connect to the server

run = True

while run:
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    clientSocket.connect(("192.168.98.76",12000));
    choice  = input("1.ADD\n2.SUB\n3.MUL\n4.DIV\n5.Simple Interest\nEnter Your Choice :")
    if choice == "1":
        data=inp()+"1"
    elif choice == "2":
        data = inp()+"2"
    elif choice == "3":
        data = inp()+"3"
    elif choice == "4":
        data = inp()+"4"
    #elif choice =="5":
        #data = simple()+"5"
    else:
        run = False
        print("Exit Initiated")
        clientSocket.close()
        exit(0)
   
    
    clientSocket.send(data.encode());
    dataFromServer = clientSocket.recv(1024);
    print(dataFromServer.decode());
    clientSocket.close()
    

    
    