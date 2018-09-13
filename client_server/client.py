from socket import *
from codecs import decode
import sys

"""
Given a set of command line arugments in the form of (linux):

python3 client.py "localhost" 8080 20 30


Note that the port specified must be the same as the one specified for server.py

The client will attempt to connect to the address specified by the port and host, and
if successful will be connected until explicitly told to stop by an empty String and [enter].
Once connected, a client can get results of simple math problems, server time, and the name
of the server.
"""

def main():
    """
    The main method gets the terminal input and connects to the server
    """
    terminal_argv = sys.argv
    if len(terminal_argv) != 5:
        print("After the python file 4 arguments are required: " +
              "host, port, two numbers for math calculations")
        sys.exit(-1)
    print(terminal_argv)
    client = Client(terminal_argv[1], terminal_argv[2])
    client.connect()
    client.loop(terminal_argv)


class Client(object):

    def __init__(self, host, port):
        """
        Client that sends messages to the server
        to get back a result based on arugments given
        :param host: Host of server
        :param port: Port of server
        :param server_name: Name of server
        """
        self.server = socket(AF_INET, SOCK_STREAM)
        self.bufsize = 1024
        self.host = host
        self.port = port
        self.address = (host, int(port))

    def connect(self):
        """
        Connect to the server
        """
        self.server.connect(self.address)

    def disconnect(self):
        """
        Disconnect from the server
        """
        self.server.close()

    def loop(self, terminal_argv):
        """
        Simple server loop which prevents disconnecting from a client
        without explicitly being told to do so.
        :param terminal_argv: Terminal arguments given
        :return: The result of the operation that is specified in the terminal arguments given.
        """
        num_args = [terminal_argv[1], terminal_argv[2], terminal_argv[3], terminal_argv[4]]
        self.send_input(num_args)
        output = self.get_output()
        print(output)
        print("\nRequest information from the server, or [enter] to exit. " +
              "Enter 'help' and [enter] to get server commands\n")
        while True:
            message = input("$ ")
            if message == "":
                self.disconnect()
                break
            self.send_arg(message)
            output = self.get_output()
            print(output)
            print("\n")

    def send_input(self, args):
        """
        Sent message to server. The args type is an array
        not an individual argument.
        :param args: Message to send
        """
        for item in args:
            # Note that the String returned in this method
            # will be joined together as one whole String
            self.server.send(bytes(item + " ", "ascii"))

    def send_arg(self, arg):
        """
        Send message to server. This method is
        a 1 argument only method not an array
        as described in the previous method.
        :param arg: Argument or message to send
        """
        self.server.send(bytes(arg, "ascii"))

    def get_output(self):
        """
        Get message back from server which will be a result
        based on the given input when sent.
        :return: The output back from there server
        """
        output = decode(self.server.recv(self.bufsize), "ascii")
        return output


if __name__ == "__main__":
    main()
