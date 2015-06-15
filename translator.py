"""
This module will encode a turing machine table into a Standard Description, SD.

A configuration (m-config + symbol) can specify one operation.

Operations are reduced to three classes (Turing 1936, p240).

Index each available of these 2 things: m-config, symbol.

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


"""

def digest_table_to_DN(turing_machine_table):





