### Simple Client Server Example in Python
This is a simple example of a Python server that communicates with a client through sockets and 
can handle multiple clients. Each client request runs on it's own thread.

### Python 3...
Scripts only work with Python 3

# Files:
server.py and client.py are the only two files needed to run in the terminal.
The other files: ClientThreader.py (ClientHandler) and Generate.py are helpers. Specifically, ClientThreader 
is the Threads used for each request and Generate just gets some basic calculations and help menu

### server.py:
For the server the arguments should be as follows:

python3 server.py MyServer 8080

MyServer is the name of the server
8080 is the port number to use, you can use any port number.

### client.py:
For a client the arguments should be as follows:

python3 client.py "localhost" 8080 20 30

localhost would be the host, but if you want you can easily use
an IP, 8080 is the port and must be the same as server.py. The two numbers
at the ned are for simple add, subtract, multiply, and dived of those two
numbers. When the client is started you can type in 'add' and press enter
and the server will return those two numbers added together.