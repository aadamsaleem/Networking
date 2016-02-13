#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
serverSocket.bind(('',8889))
serverSocket.listen(1)
while True:
    #Establish the connection
    print 'Ready to serve...'
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        print filename
        f = open(filename[1:])
        outputdata = f.read()
        #Send one HTTP header line into socket
        connectionSocket.send('HTTP/1.0 200 OK\r\n')
        connectionSocket.send("Content-Type: text/html\r\n\r\n")
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.close()
    except IOError:
            #Send response message for file not found
            print 'Error 404 : File "..' + filename + '" not found'
            connectionSocket.send('Error 404 : File not found\n')
            connectionSocket.send('Requested File : ' + filename)
            #Close client socket
            connectionSocket.close()
serverSocket.close()
