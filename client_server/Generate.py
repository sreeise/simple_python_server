"""
File for returing messages to back to the client. This class/file generates the message but
does not send them.
"""

help_arguments = str("1. $ name\n\tGet the name of the server\n2. $ help\n\tReturns list of help commands" +
                     "\n3. $ servertime\n\tReturns time of server" +
                     "\n4. $ add\n\tReturns add(x, y) = x + y" +
                     "\n5. $ sub\n\tReturns sub(x, y) = x - y" +
                     "\n6. $ mult\n\tReturns mul(x, y) = x * y" +
                     "\n7. $ div\n\tReturns div(x, y) = x / y" +
                     "\n8. $ math\n\tReturns add, sub, mul, and div")

math_args = ["add", "sub", "mult", "div", "math"]


class Generate(object):

    def __init__(self, num1, num2):
        self.num1 = float(num1)
        self.num2 = float(num2)
        # We can take advantage of memoization here by
        # only computing these values once, and storing
        # for the life of the current object. Returning
        # the stored variable instead of redoing the calculation.
        self.add = self.add()
        self.sub = self.sub()
        self.mult = self.mult()
        self.div = self.div()

    def get_host(self):
        """
        :return: Host for connection
        """
        return self.host

    def get_port(self):
        """
        :return: Port number of server
        """
        return self.port

    def get_num1(self):
        """
        :return: The first number given to a Generate
        object that can be used for getting simple
        mathematical results.
        """
        return self.num1

    def get_num2(self):
        """
        :return: The second number given to a Generate
        object that can be used for getting simple
        mathematical results.
        """
        return self.num2

    def getMessage(self, message):
        """
         Recieves a message from the thread, and
         from here it can either be 1 on 3 arguments.
         1. Show the help arugments
         2. A math quesiton
         3. An argument that is not a part of the program, and
         in this case, a message indicating so is given back
        :param message: The command line argument representing
                        a method.
        :return: String result of the method representation or
                a error message based on what the arugments given are.
        """
        if message == "help":
            return self.help()
        else:
            for math_op in math_args:
                if math_op == message:
                    return str(self.calculate(message))
        return "Could not identify argument given"

    def math_prob_reply(self, message):
        return str(self.calculate(message))

    def add(self):
        """
        :return: Result of two numbers added together
        """
        return self.get_num1() + self.get_num2()

    def sub(self):
        """
        :return: Result of subtracting two numbers
        """
        return self.get_num1() - self.get_num2()

    def mult(self):
        """
        :return: Multiplied result of two numbers
        """
        return self.get_num1() * self.get_num2()

    def div(self):
        """
        :return: Dividend of two numbers
        """
        if self.get_num1() == 0:
            return 0
        return self.get_num1() / self.get_num2()

    def calculate(self, arg):
        """
        The math method indicated by the argument
        :param arg: Name of the math method
        :return: Result of math method
        """
        if arg == "add":
            return self.add
        elif arg == "sub":
            return self.sub
        elif arg == "mult":
            return self.mult
        elif arg == "div":
            return self.div
        elif arg == "math":
            return self.calculate_all()
        return "No matching arguments found"

    def calculate_all(self):
        """
        :return: Somewhat like a toString() method in languages like Java where
                all four simple math problems are returned in a String with their name
        """
        message = str("Addition: {0}\nSubtraction: {1}\nmultiplication: {2}\nDivision: {3}"
                      .format(self.add, self.sub, self.mult, self.div))
        return message

    def help(self):
        """
        :return: The command line options for a client
        """
        return help_arguments
