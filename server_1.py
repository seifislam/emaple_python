import socket #this server only does recv data ,if you have ideas, change
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#this server is TCP 
server.bind((host,port))
server.listen(1)
print 'server is run at {}:{}'.format(host,port)
######## to do ########
client,addr = server.accept()
data = client.recv(4096)
print data
