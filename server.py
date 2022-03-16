import socket

# Create a stream based socket(i.e, a TCP socket)

# operating on IPv4 addressing scheme

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

# Bind and listen

serverSocket.bind(("192.168.98.76", 12000));

serverSocket.listen(4);

# Accept connections
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
   s=[]
   j=0
   d=int(f[0])-int(f[1])
   return d

def div1(f):
    a=int(f[0])
    b=int(f[1])
    d=a/b
    return d



while (True):
    (clientConnected, clientAddress) = serverSocket.accept();

    print("Accepted a connection request from %s:%s" % (clientAddress[0], clientAddress[1]));

    dataFromClient = clientConnected.recv(1024)

    d=dataFromClient.decode()
    f=d.split(',')
    n=len(f)

    if  f[n-1]=='1':
        sum1=add1(f)

    elif f[n-1]=='2':
        sum1=sub1(f)
    elif f[n-1]=='3':
        sum1=mul1(f)
    elif f[n-1]=='4':
        sum1=div1(f)
    else:
        sum1=-1
    # Send some data back to the client
    sum2 = str(sum1);

    clientConnected.send(sum2.encode())
    clientConnected.close()
