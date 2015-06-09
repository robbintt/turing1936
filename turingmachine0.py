"""

"""
import instructions




# Make a machine
turing_machine_0 = turing_machine()

# This doesn't take into account scanned symbol yet.
# With scanned symbol, the table takes on more complexity.
turing_machine_0.operations = {
        'b' : (['P0','R'],'c'),
        'c' : ('R','e'), 
        'e' : (['P1','R'],'f'),
        'f' : ('R','b')
        }

turing_machine_0.instructions = {
        'P0' : instructions.print_zero,
        'P1' : instructions.print_one,
        'R' : turing_machine_0.scan_to_right,
        'L' : turing_machine_0.scan_to_left
        }


