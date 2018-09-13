from codecs import decode
from threading import Thread
from Generate import Generate
import sys
from time import ctime


"""
ClientHandler is the Thread class which communicates with the client.

Press [enter] with no arguments (empty String), to shutdown the current thread.
"""

BUFSIZE = 1024
CODE = "ascii"


class ClientHandler(Thread):
    """Thread handler for client/server"""

    def __init__(self, client, servername):
        """
        Constructor for ClientHandler which takes a client and the
        name of the server.
        :param client: Socket connection from client to server
        :param servername: Name of the server specified by a command
                            line argument
        """
        Thread.__init__(self)
        self.client = client
        first_message = decode(self.client.recv(BUFSIZE))
        message = first_message.split(" ")
        self.generate = Generate(message[2], message[3])
        self.servername = servername

    def run(self):
        """
        Loop for each thread. The thread runs until the client disconnects.
        Each time a message is sent, this method will hand off the message
        to method send_on_message()
        """
        try:
            self.client.send(bytes("\nCONNECTED\n", CODE))
            while True:
                message = decode(self.client.recv(BUFSIZE), CODE)
                self.send_on_message(message)
                # The ~# line is for the client to tell the
                # thread that they want to close the connection
                if message == "~#" or not message:
                    print("Client disconnected")
                    self.client.close()
                    sys.exit(0)
        except KeyboardInterrupt:
            self.client.close()
        except OSError:
            print("Attempted to get message, however, either a keyboard interrupt caused a stop" +
                  " or arguments given caused an error, shutting down current thread")
            self.client.close()
        except BrokenPipeError:
            print("Interrupts caused failed execution shutting down current thread")
            self.client.close()

    def send_on_message(self, message):
        """
        message request come through here. If either the server time or
        the name of the server is requested, this information is given
        by the thread helper itself, else all other methods are done through
        class Generate
        :param message: Command from input
        :return: Information based off of command
        """
        if message == "name":
            self.client.send(bytes(self.servername, CODE))
        elif message == "servertime":
            self.client.send(bytes(ctime(), CODE))
        else:
            message = self.generate.getMessage(message)
            if message is None:
                self.client.send(bytes("Could not identify argument given", CODE))
            else:
                self.client.send(bytes(message, CODE))
