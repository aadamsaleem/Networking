import socket
import base64

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
#Fill in start
mailserver = "smtp.gmail.com"
port = 587
#Fill in end

# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
clientSocket = socket.socket()
clientSocket.connect((mailserver, port))
#Fill in end

recv = clientSocket.recv(1024)
print recv
if recv[:3] != '220':
        print '220 reply not received from server.'

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
 print '250 reply not received from server.'

#ADDITIONAL FOR GMAIL SERVER START

recipient = "<as9749@nyu.edu>"
sender = "<aadam.saleem@gmail.com>"
username = "aadam.saleem"
password = 'zenith2horizon'

#Request an encrypted connection
startTlsCommand = 'STARTTLS\r\n'
clientSocket.send(startTlsCommand)
tlsReply = clientSocket.recv(1024)
print tlsReply
if tlsReply[:3] != '220':
	print '220 reply not received from server'

#Encrypt the socket
sslClientSocket = socket.ssl(clientSocket)

#Send the AUTH LOGIN command and print server response.
authCommand = 'AUTH LOGIN\r\n'
sslClientSocket.write(authCommand)
authReply = sslClientSocket.read(1024)
print authReply
if authReply[:3] != '334':
	print '334 reply not received from server'

#Send username and print server response.
username = base64.b64encode(username) + '\r\n'
sslClientSocket.write(username)
usernameReply = sslClientSocket.read(1024)
print usernameReply
if usernameReply[:3] != '334':
	print '334 reply not received from server'

#Send password and print server response.
password = base64.b64encode(password) + '\r\n'
sslClientSocket.write(password)
passwordReply = sslClientSocket.read(1024)
print passwordReply
if passwordReply[:3] != '235':
	print '235 reply not received from server'	
#ADDITIONAL FOR GMAIL SERVER END

# Send MAIL FROM command and print server response.
#Fill in start
mailFromCommand = 'MAIL FROM: ' + sender + '\r\n'
sslClientSocket.write(mailFromCommand)
reply = sslClientSocket.read(1024)
print reply
if reply[:3] != '250':
    print '250 reply not received from server.'
#Fill in end

# Send RCPT TO command and print server response.
#Fill in start
rcptToCommand = 'RCPT TO: ' + recipient + '\r\n'
sslClientSocket.write(rcptToCommand)
reply = sslClientSocket.read(1024)
print reply
if reply[:3] != '250':
    print '250 reply not received from server.'
#Fill in end

# Send DATA command and print server response.
#Fill in start
dataCommand = 'DATA\r\n'
sslClientSocket.write(dataCommand)
reply = sslClientSocket.read(1024)
print reply
if reply[:3] != '354':
    print '354 reply not received from server.'
#Fill in end

# Send message data.
#Fill in start
sslClientSocket.write(msg)
#Fill in end

# Message ends with a single period.
#Fill in start
sslClientSocket.write(endmsg)
reply = sslClientSocket.read(1024)
print reply
if reply[:3] != '250':
    print '250 reply not received from server.'
#Fill in end

# Send QUIT command and get server response.
#Fill in start
quitCommand = 'QUIT\r\n'
sslClientSocket.write(quitCommand)
reply = sslClientSocket.read(1024)
print reply
if reply[:3] != '221':
    print '221 reply not received from server.'

clientSocket.close()
#Fill in end
