from socket import *
from ClientThreader import ClientHandler
import sys

"""
server.py is the main interface that accepts requests through the port specified when running
the file. Each request is set on a new thread, and handled independently.

Because the server must continually listen, and threads run simultaneously, the server
can only shutdown by Ctrl C and when there are no threads running, or another combination
that invokes KeyBoardInterruptError and the server will shutdown. The server catches
the exception and closes, however, if there are threads running this will cause errors

server.py accepts 4 arguments including the python file itself as (linux):

python3 server.py MyServer 8080

Note that the port specified must be the same as the one specified for client.py
"""

def main():
    """
    Stars a new Server object and listener
    """
    terminal_argv = sys.argv
    if len(terminal_argv) != 3:
        print("After the python file 2 arguments are required: " +
              "server name and port number for server to listen on")
        sys.exit(-1)
    server = Server(terminal_argv)
    server.runner()


class Server(object):
    """
    Server that listens for requests
    """

    def __init__(self, args):
        """
        Sets the data needed server
        :param args:
        """
        self.HOST = "localhost"
        self.PORT = int(args[2])
        self.ADDRESS = (self.HOST, self.PORT)
        self.args = args
        self.server_name = str(args[1])
        self.server = socket(AF_INET, SOCK_STREAM)
        self.server.bind(self.ADDRESS)
        self.server.listen(5)

    def runner(self):
        """
        Waits for requests and starts each Client on a new thread
        The server socket only listens for the request, while
        the individual threads take care of the actual work.
        """
        try:
            print("\nWhen a thread is not connected, press Ctrl C " +
                  "with no arguments to shutdown the server\n")
            while True:
                print("Waiting for connection...")
                client, address = self.server.accept()
                handler = ClientHandler(client, self.server_name)
                handler.start()
                print("\n... connected from:", address)
                print("On IP, Port:", client.getsockname())
                print("")
        except KeyboardInterrupt:
            self.server.close()
            sys.exit(0)
        except OSError:
            print("Attempted to get message, however, either a keyboard interrupt caused a stop,\n" +
                  "or arguments given caused an error, server shutting down. Original Error: OSError")
            self.server.close()
        except BrokenPipeError:
            print("Interrupts caused failed execution, server shutting down. Original Error: BrokenPipeError")
            self.server.close()

    def close_server(self):
        self.server.close()


if __name__ == "__main__":
    main()
