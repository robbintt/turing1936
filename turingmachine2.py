"""
The second turing machine in Turing's 1936 paper.

Simplifies the first machine by allowing multiple L and R actions in a single entry.
"""
import instructions # Some simple instructions (functions) from Turing 1936.
import amachine # Generic Turing Machine per Turing 1936.

import time # used for the clock in the while loop (see bottom)
import logging # Log results

# Make a turing machine
turing_machine = amachine.turing_machine()

# Set the initial m-configuration
# Scanned symbol starts at blank square by default.
turing_machine.m_config = 'b'

# A single space represents an empty square.
# An any string, 'any', represents 'any square'
turing_machine.operations = {
        'b' : {
            ' ' : (['Pe','R','Pe','R','P0','R','R','P0','L','L'],'o')
        },
        'o' : {
            '1' : (['R','Px','L','L','L'], 'o'),
            '0' : ([], 'q')
        },
        'q' : {
            # next two lines are 'any(0 or 1)' in Turing 1936 p234
            '0' : (['R','R'],'q'),
            '1' : (['R','R'],'q'),
            ' ' : (['P1','L'],'p')
        },
        'p' : {
            # The E, erase, function has been replaced by 'P ', print space
            # In our lexicon, a single space is an empty square.
            'x' : (['P ','R'],'q'),
            'e' : (['R'],'f'),
            ' ' : (['L','L'],'p')
        },
        'f' : {
            # edge case, we want to process ' ' with a higher priority than any
            'any' : (['R','R'],'f'),
            ' '   : (['P0','L','L'],'o')
        }
    }

turing_machine.instructions = {
        'Pe' : turing_machine._print,
        'Px' : turing_machine._print,
        'P0' : turing_machine._print,
        'P1' : turing_machine._print,
        # The erase instruction is replaced by a print space instruction
        # This is equivalent, since our empty space is a single space: ' '
        'P ' : turing_machine._print,

        'R' : turing_machine.scan_to_right,
        'L' : turing_machine.scan_to_left
        }

# The turing machine just keeps going unless a stop operation is defined.
i = 0 # count number of while loops... (# of configurations processed)
while True:
    time.sleep(0.25)
    logging.debug("===== Behavior Sequence #: {} =====".format(i))
    logging.debug("m-config: {}".format(turing_machine.m_config))
    logging.debug("left tape: {}".format(turing_machine.left_tape))
    logging.debug("Scanned Symbol: {}".format(turing_machine.scanned_symbol))
    logging.debug("right tape: {}".format(list(reversed(turing_machine.right_tape))))

    turing_machine.ingest_behavior()
    i += 1 # increment configuration/loop counter
