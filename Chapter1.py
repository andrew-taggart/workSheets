# Logical Operations
#

def logical_and(p, q):
    return p and q

def logical_or(p, q):
    return p or q

def logical_not(p):
    return not p

def implication(p, q):
    # Equivalent to "p -> q", which is "(not p) OR q"
    return not p or q

def biconditional(p, q):
    # Equivalent to "p <-> q", which is "(p AND q) OR (not p AND not q)"
    return (p and q) or (not p and not q)

#Truth Tables

def truth_table():
    # List of all possible truth values for p and q
    values = [(True, True), (True, False), (False, True), (False, False)]
    
    #Header for the table
    print(f"{'p':<5} {'q':<5} {'p AND q':<10} {'p OR q':<10} {'NOT p':<10} {'p -> q':<10} {'p <-> q':<10}" )
    print('-' * 60)
    
    # Loop over all possible values for p and q
    # str() to convert boolean values to strings explicitly
    for p, q in values:
        print(f"{str(p):<5} {str(q):<5} {str(logical_and(p, q)):<10} {str(logical_or(p, q)):<10} {str(logical_not(p)):<10} {str(implication(p, q)):<10} {str(biconditional(p, q)):<10}")
        
#Display Truth table
truth_table()

# Logical Equivalence Check

def check_equivalence():
    values = [(True, True), (True, False), (False, True), (False, False)]
    
    equivalent = True
    for p, q in values:
        prop1 = implication(p, q)
        prop2 = logical_or(logical_not(p), q)
        
        if prop1 != prop2:
            equivalent = False
            break
        
    return equivalent

# Test equivalnce
if check_equivalence():
    print("p -> is equivalent to NOT-p OR q")
else:
    print("p -> is not equivalent to NOT-p OR q")