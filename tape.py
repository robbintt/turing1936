"""



"""

class turing_machine(object):
    """
    Machine:
    The machine can hold a tape. It can hold one m-configuration and read the symbol in the Scanned Square.

    Tape: 
    The tape has unlimited length, each position can hold one symbol.

    Scanned Square: 
    The position on the tape that can currently be scanned.

    Scanned Symbol:
    The scanned symbol can be erased, left blank, written over.

    m-configuration:
    The m-configuration is a state the machine stores inside itself.

    Configuration:
    The Scanned Symbol and m-configuration combine and become the Configuration.

    Determining Behavior:
    The Configuration determines the next operations.
    The Configuration determine the next m-configuration.

    Actions:
    The machine may shift the tape one position to the right.
    The machine may shift the tape one position to the left.
    The machine may erase the scanned symbol.
    The machine may write a symbol on the scanned square, if empty.





    As a result: 
            we will refer to the scanned symbol once per cycle.
            we will refer to the m-configuration once per cycle.

    How should a tape be qualified?
    1. It could be a list with an index stored as the 'scanned square'
    2. It could be a variable which is popped off left and onto right. This approach requires maintaining two strings, one of which increases to the left, one of which increases to the right.
    3. 
    """


    def __init__(self):
        self.tape = ""
        


