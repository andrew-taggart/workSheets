# Logical Operations

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

