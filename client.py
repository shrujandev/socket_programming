
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


def diventry():
    val1 = input("Enter Divident")
    val2 = input("Enter Divisors")
    return str(val1)+','+str(val2)

def simple():
    princ = input("Enter Principal Amount")
    time = input("Enter Time in Years")
    rate = input("Enter Rate of Interest")
    return str(princ)+','+str(time)+','+str(rate)

def compoundint():
    princ = input("Enter Principal Amount : ")
    time = input("Enter Time in Years : ")
    rate = input("Enter Rate of Interest : ")
    n = input("Interest Applied Per time Period : ")
    return str(princ)+','+str(time)+','+str(rate)+','+str(n)


    
def numericalcal():
    run = False
    while run:
        os.system('cls')
        choice  = input("1.Addition\n2.Substraction\n3.Multiplication\n4.Division\n5.Main Menu\nEnter Your Choice :")
        if choice == "1":
            data=inp()+"1"
        elif choice == "2":
            data = inp()+"2"
        elif choice == "3":
            data = inp()+"3"
        elif choice == "4":
            data = diventry()+"4"
        elif choice == "5":
            mainmenu()
        else:
            print("Wrong Entry ...")

        if run == False:
            return data
    
def fincal():
    run = True
    while run:
        os.system('cls')
        choice  = input("1.Simple Interest\n2.Compound Interest\n3.Main Menu\nEnter Your Choice :")
        if choice == "1":
            data=simple()+"5"
        elif choice == "2":
            data = compoundint()+"6"
        elif choice == "3":
            mainmenu()
        else:
            print("Wrong Entry ...")
            run = False
        return data


serverIP =  ""
print("Connecting to server ...\n")




clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
clientSocket.connect((serverIP,12000))
print("Connection Established\n")
time.sleep(3)
os.system('cls')

# Connect to the server

def mainmenu():
    run = True

    while run:
        os.system('cls')
        choice  = input("Main Menu\n1.Simple Calculator\n2.Trignometric Calculator\n3.Financial Calculator\n4.Exit\nEnter Your Choice :")
        if choice == "1":
            data=numericalcal()
        elif choice == "2":
            data = trigcal()
        elif choice == "3":
            data = fincal()
        elif choice == "4":
            run = False
            print("Exit Initiated...")
            clientSocket.close()
            exit(0)
        else:
            print("Invalid Choice...")
            time.sleep(3)
   
    
    clientSocket.send(data.encode());
    dataFromServer = clientSocket.recv(1024);
    print(dataFromServer.decode());
    clientSocket.close()
