"""
The second turing machine in Turing's 1936 paper.

Simplifies the first machine by allowing multiple L and R actions in a single entry.
"""
import instructions # Some simple instructions (functions) from Turing 1936.
import amachine # Generic Turing Machine per Turing 1936.
import time # used for the clock in the while loop (see bottom)

# Make a turing machine
turing_machine = amachine.turing_machine()

# Set the initial m-configuration
turing_machine.m_config = 'b'

# A single space represents an empty square.
# An any string, 'any', represents 'any square'
turing_machine.operations = {
        'b' : {
            ' ' : (['P0'],'b'),
            '0' : (['R','R','P1'],'b'),
            '1' : (['R','R','P0'],'b')
        },
    }

turing_machine.instructions = {
        'P0' : turing_machine._print,
        'P1' : turing_machine._print,
        'R' : turing_machine.scan_to_right,
        'L' : turing_machine.scan_to_left
        }

# The turing machine just keeps going unless a stop operation is defined.
while True:
    time.sleep(0.25)
    turing_machine.ingest_behavior()

