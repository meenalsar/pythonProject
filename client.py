import socket               # Import socket module

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)         # Create a socket object
host = socket.gethostname() # Get local machine name
port1= 12345                #port number for face detection
port2= 12346                #port number for face recognition
port = int(input("Select a port number either 12345(Detection) or 12346(Recognition): "))                           

s.connect((host, port))

while port==12345 and True:

	print(s.recv(1024))
	data = input();
	s.send(data.encode())

s.recv(1024);
s.close()                     # Close the socket when done