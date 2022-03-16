
import socket
import  os
import time 

def inp():
    dataString=''
    num = int(input("Enter The Number of Elements"))
    for i in range(num):
        val = input("Enter Numbers : ")
        dataString = dataString +','+ str(val)
    return dataString

def simple():
    princ = input("Enter Principal Amount")
    time = input("Enter Time in Years")
    rate = input("Enter Rate of Interest")

    return str(princ)+','+str(time)+','+str(rate)


    
def numericalCal():
    run = True
    while run:
        choice  = input("1.Addition\n2.Substraction\n3.Multiplication\n4.Division\n5.Main Menu\nEnter Your Choice :")
        if choice == "1":
            data=inp()+"1"
        elif choice == "2":
            data = inp()+"2"
        elif choice == "3":
            data = inp()+"3"
        elif choice == "4":
            data = inp()+"4"
        else:
            run = False
            print("Exit Initiated")
            clientSocket.close()
            exit(0)
    
    

print("Enter Server Details\n")
serverIP =  input("Enter Server IP : ")
print("Connecting to server ...\n")




clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
clientSocket.connect((serverIP,12000))
print("Connection Established\n")
time.sleep(3)
os.system('cls')

# Connect to the server

run = True

while run:
    choice  = input("Welcome to Main Menu\n1.Simple Calculator\n2.Trignometric Calculator\n3.Financial Calculator\n4.Exit\nEnter Your Choice :")
    if choice == "1":
        data=numericalCal()
    elif choice == "2":
        data = inp()+"2"
    elif choice == "3":
        data = inp()+"3"
    elif choice == "4":
        data = inp()+"4"
    elif choice =="5":
        data = simple()+"5"
    else:
        run = False
        print("Exit Initiated")
        clientSocket.close()
        exit(0)
   
    
    clientSocket.send(data.encode());
    dataFromServer = clientSocket.recv(1024);
    print(dataFromServer.decode());
    clientSocket.close()
