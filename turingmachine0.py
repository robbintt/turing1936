"""

"""
import instructions # Some simple instructions (functions) from Turing 1936.
import amachine # Generic Turing Machine per Turing 1936.

# Make a turing machine
turing_machine_0 = amachine.turing_machine()

# Set the initial m-configuration
turing_machine_0.m_config = 'b'

# A single space represents an empty square.
# An any string, 'any', represents 'any square'
turing_machine_0.operations = {
        'b' : {
            ' ' : (['P0','R'],'c')
        },
        'c' : {
            ' ' : ('R','e'), 
        },
        'e' : {
            ' ' : (['P1','R'],'f'),
        },
        'f' : {
            ' ' : ('R','b')
        }
    }

turing_machine_0.instructions = {
        'P0' : instructions.print_zero,
        'P1' : instructions.print_one,
        'R' : turing_machine_0.scan_to_right,
        'L' : turing_machine_0.scan_to_left
        }

# The turing machine just keeps going unless a stop operation is defined.
while True:
    turing_machine_0.ingest_behavior()

