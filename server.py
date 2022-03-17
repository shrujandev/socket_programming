import opcode
import socket
import threading
import math


HOST = "localhost"
PORT = 12000

def add1(f):
    n=len(f)
    s=0
    for i in range(0,n-1):
        s=s+int(f[i])
    return s

def mul1(f):
    n=len(f)
    s=1
    for i in range(0,n-1):
        s=s*int(f[i])
    return s

def sub1(f):
    n=len(f)
    s = int(f[0])
    for i in range(0,n-1):
        s=s-int(f[i])
    return s

def div1(f):
    a=int(f[0])
    b=int(f[1])
    d=a/b
    return d


def simple(f):
    p = int(f[0])
    t = int(f[1])
    r = int(f[2])
    return p*t*r/100

def compound(f):
    p = int(f[0])
    t = int(f[1])
    r = int(f[2])
    n = int(f[3])
    d=(1+r/(100*n))
    q = n*t
    return p*(math.pow(d,q))



def keepalive(clientConnected,clientAddress):
    print("Accepted a connection request from %s:%s" % (clientAddress[0], clientAddress[1]))
    dataFromClient = clientConnected.recv(1024)
    d=dataFromClient.decode()
    f=d.split(',')
    n=len(f)
    opCode = f[n-1]
    if  opCode=='1':
        result=add1(f)
    elif opCode=='2':
        result=sub1(f)
    elif opCode=='3':
        result=mul1(f)
    elif opCode=='4':
        result=div1(f)
    elif opCode == '5':
        result = simple(f)
    elif opCode == '6':
        result = compound(f)
    elif opCode == '7':
        result = math.sin(f[0])
    elif opCode == '8':
        result = math.cos(f[0])
    elif opCode == '9':
        result =math.tan(f[0])
    else:
        result=-1            
                # Send some data back to the client
    sum2 = str(result);
    clientConnected.send(sum2.encode())    
    clientConnected.close()                        

    

    


def listenconnections():
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    serverSocket.bind((HOST, PORT));
    while True:
        serverSocket.listen(4)
        (clientConnected, clientAddress) = serverSocket.accept();
        persistantThread = threading.Thread(target =keepalive ,args =(clientConnected,clientAddress))
        persistantThread.start()




if __name__ == '__main__':
    SERVER = threading.Thread(target = listenconnections)
    SERVER.start()
    print("Server Started")



