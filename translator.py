"""
This module will encode a turing machine table into a Standard Description, SD.

A configuration (m-config + symbol) can specify one operation.

Operations are reduced to three classes (Turing 1936, p240).

Index each available of these 2 things: m-config, symbol.
Turing explicitly states that S0=blank, S1=0, S2=1

Special cases:
    An empty square is S0, an erasure is replaced with write S0.
    No write on symbol j is replaced by write Sj.

Thus 3 classes (where k is a free integer in the range indexed symbols):
    Print S(k) and move left (L).
    Print S(k) and move right(R).
    Print S(k) and do not move().

A line of a turing machine table follows this order: 
    m-config, Symbol, Operation, Final m-config

Thus each line of a turing machine table may have four free variables:
    i, j, k, m where a line of the table is: qi Sj PSk(actions) qm

The result will be called a 'reduced table' (wholly defined in Turing 1936, p240).

Some implemetation ideas - TAR 061415:
A reduced table may be produced by providing a new m-config for each step of a
complex operation.
Take the operation RRRR(P0)LLLL. Because the first three right operations must 
never alter the underlying symbol, they can be given a unique m-configration each, for
which all symbols pass the configuration along. This is a subroutine of sorts. Turing
says explicitly on p239 that the table can enter the reduced form by adding an arbitrary
number of m-configurations.
IS THIS INTERPRETATION CORRECT: Furthermore, if we obey Turing's constraints, no blank squares will exist and alternate squares will always add a new unique m-configuration.

"""

# This is turingmachine0.py in reduced form. See p241.
# The data structure is the same as used in turingmachine2.py
# Here we've organized each m-config to be a key, with a corresponding value.
# Each value is a dict with a set of keys which represent each possible symbol.
# The value of each symbol is the operation the m-config+symbol, or configuration, yields.
# Since we are always printing now, we exclude the P, giving only the printed symbol.
machine1 = {
        'q1' : { 'S0' : (['S1', 'R'],'q2') },
        'q2' : { 'S0' : (['S0', 'R'],'q3') },
        'q3' : { 'S0' : (['S2', 'R'],'q4') },
        'q4' : { 'S0' : (['S0', 'R'],'q1') } }

# See Turing 1936, p240
symbol_key = {
        'S0' : ' ',
        'S1' : '0',
        'S2' : '1' }


def digest_table_to_DN(table):
    """ Accept a turing machine table in dictionary format and return DN string.
    
    This function consumes a reduced table, allowing only the three atomic operations.

    The input table is basically a dictionary with two keys, I have used a nested dictionary
    setup in python, but I wonder if there isn't a double-keyed dictionary or n-keyed
    dictionary used frequently in algorithms. TAR 061415

    First create an indexed set of m-config and symbol.

    Find the values of D, C, A, as per p240-242.
    D - begin m-config. # of As = index of m-config
    C = begin symbol, # of As = index of symbol.
    The values L,R,N refer to whether the machine changes symbols.
    A semicolon symbol delineates the border between two rows of the table.
    The description is finally converted to a description number, DN, on these
    indexes (as python list, but start index at 1): [A, C, D, L, R, N, ;]
    """

    mconfigs = table.keys()

    symbols = []
    for mconfig in table.keys(): # go through each m-config
        symbols.extend(table[mconfig].keys()) # get all the config symbols for each m-config
        for symbol in table[mconfig].keys():
            symbols.append(table[mconfig][symbol][0][0]) # add each printed symbol
    symbols = list(set(symbols)) # simple deduplicator

    # Sorting these makes the index identical to Turing 1936, p241
    mconfigs = sorted(mconfigs)
    symbols = sorted(symbols)
    print mconfigs
    print symbols

    # Loop over each table, appending each line to the DN_string
    # A DN_string is the table row's DN characters before conversion to arabic numbers.
    DN_string = ""
    for mconfig in table.keys():
        table_line_DN_string = ""
        for symbol in table[mconfig].keys():
            # The operation is still a list, albeit here it is simply [P0, R] or somesuch.
            symbol_printed = table[mconfig][symbol][0][0]
            operation_action = table[mconfig][symbol][0][1] # already DN_string formatted
            final_mconfig = table[mconfig][symbol][1]
            
            # Turing's symbols' indexes start at 0
            # Turing's m-configurations' indexes start at 1
            mconfig_index = mconfigs.index(mconfig) + 1
            symbol_index = symbols.index(symbol)
            symbol_printed_index = symbols.index(symbol_printed)
            final_mconfig_index = mconfigs.index(final_mconfig) + 1

            table_line_DN_string =  "D" + "A"*mconfig_index + "D" + "C"*symbol_index + \
                                    "D" + "C"*symbol_printed_index + operation_action + \
                                    "D" + "A"*final_mconfig_index + ";"

            DN_string += table_line_DN_string

    # Note this extra uniqueness constraint:
    # index of each symbol must be incremented by one. This table must have all unique
    # entries because it is used as a lookup table for the index.
    DN_table = ['A', 'C', 'D', 'L', 'R', 'N', ';']
    DN = ""
    for letter in DN_string:
        DN += str(DN_table.index(letter) + 1)

    #return DN_string
    return DN


print "Note that the DN need not be ordered on rows as turing's paper has them."
print "These DN are stored unordered, so they must be crossmatched to verify the paper."
print digest_table_to_DN(machine1)


