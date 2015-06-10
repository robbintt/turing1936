"""
Generic Turing Machine

This machine needs operations, instructions, and an ingestion loop.

operations:
    a dictionary of functions that perform defined operations
    the keys are strings and are stored in the instructions

ingestion loop:
    a for loop that repeatedly ingests the machine configuration
    the configuration is available internally so this is just:
    while True:
        mymachine.ingest_behavior()
"""
import logging

logging.basicConfig(level=logging.DEBUG)


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

    How should a tape be qualified? (i chose option 2)
    1. It could be a list with an index stored as the 'scanned square'
    2. It could be a variable which is popped off left and onto right. This approach requires maintaining two strings, one of which increases to the left, one of which increases to the right.
    
    Each configuration needs a sequential list of instructions and the next m-configuration.

    How should Configuration instructions be managed?
    1. Configuration is a sequential list of actions finally providing the next state.
    2. It follows that state is a 'named sequence' best represented by a key-value pair.
    3. The key is the name of the m-configuration.
    4. The value is a tuple, V. V[0] is a list of instructions, V[1] is name of next m-configuration.
    5. V[0] is a list of keys (instructions) whose values are functions in a lookup table (dictionary).
    """


    def __init__(self):
        """
        This class is a general representation of a turing machine.
        m-configuration and operations must be defined outside this class.

        Note that the empty symbol is a space in this implementation.
        """
        self.m_config = ""
        self.operations = {}

        # One method of managing the tape is to individually manage the left and right
        # sides of the tape. The ordinality of the tape is defined as such:
        # tape[i] can be popped or appended. The last item is always the closest to the scanner.
        # This is a complete description because the tape has only one reference. The scanner.
        self.left_tape = list()
        self.right_tape = list()
        self.scanned_symbol = " "

        self._print_symbol = ""


    def scan_to_right(self, *args, **kwargs):
        """
        """
        # Store current scanned symbol on the other tape.
        self.left_tape.append(self.scanned_symbol)
        
        try:
            self.scanned_symbol = self.right_tape.pop()
        except IndexError:
            # If the list is empty, generate an empty space.
            self.scanned_symbol = " "

    def scan_to_left(self, *args, **kwargs):
        """
        """
        # Store current scanned symbol on the other tape.
        self.right_tape.append(self.scanned_symbol)
        
        try:
            self.scanned_symbol = self.left_tape.pop()
        except IndexError:
            # If the list is empty, generate an empty space.
            self.scanned_symbol = " "

    def _print(self, *args, **kwargs):
        """ Print the instruction_symbol onto the scanned square.
        """

        # The last letter of the print symbol. This function only receives strings.
        self.scanned_symbol = args[0][-1]
        logging.debug("Print to tape:" + self.scanned_symbol)


    def ingest_behavior(self):
        """ Process the current configuration's operations.

        Ingestion symbol prioritization:
        ' ' is empty, and is ingested if it is set.
        'any' matches all other symbols. It is ingested if it exists.
        Finally, the specific symbol is matched.
        An error is thrown if the symbol isn't in the table.
        """

        if self.scanned_symbol == ' ':
            try:
                configuration = self.operations[self.m_config][' ']
            except KeyError:
                logging.critical("Unspecified Configuration: {} {}".format(self.m_config, self.scanned_symbol))
        else:
            try:
                configuration = self.operations[self.m_config]['any']
            except KeyError:
                pass # any is not required

            try:
                configuration = self.operations[self.m_config][self.scanned_symbol]
            except KeyError:
                logging.critical("Unspecified Configuration: {} {}".format(self.m_config, self.scanned_symbol))


        # Reverse operations so the last operation has the index 0.
        # This allows us to pop() the last off in O(1) time.
        operations = list(reversed(configuration[0]))
        next_m_config = configuration[1]

        # Chew up the list of operations until it is empty.
        while len(operations):
            current_operation = operations.pop() # the list was reversed at the top of this method.

            # Apply the function corresponding to the operation
            if current_operation in self.instructions.keys():
                self.instructions[current_operation](current_operation)

        # set the new m-configuration
        self.m_config = next_m_config
        return
