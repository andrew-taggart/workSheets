## Basic Structures
## 2.1 and 2.2 Sets and Set Properties

# Defining a set in Python
my_set = {1, 2, 3, 4}
print(my_set)
# Elements of a set must be unique, duplicates won't be counted twice


##Set Operations
A = {1,2,3}
B = {3,4,5}
# Set UNION; Math Notation: A ∪ B
union_set = A.union(B)
print(union_set)
#Set INTERSECTION; Math Notation: A ∩ B
intersection_set = A.intersection(B)
print(intersection_set)
#Set DIFFERENCE; Math Notation: A − B
#The difference between two sets contains elements that are in the first set but not in the second.
difference_set = A.difference(B)
print(difference_set)
#Set SYMMETRIC DIFFERENCE; Math Notation A Δ B
#The symmetric difference contains elements that are in either of the sets, but not in both.
symmetric_difference_set = A.symmetric_difference(B)
print(symmetric_difference_set)

#SUBSET: Set A is a subset of set B if all elements of A are also in B.
# Math Notation A ⊆ B
X = {1, 2}
Y = {1, 2, 3, 4}
is_subset = X.issubset(Y)
other_subset = A.issubset(B)
print(is_subset)
print(other_subset)
#SUPERSET: Set A is a superset of set B if all elements of B are also in A
is_superset = B.issuperset(A)
other_superset = Y.issuperset(X)
print(is_superset)
print(other_superset)


##Set Properties

#Commutative Property
#Union example: A∪B = A∪B
#Intersection example: A∩B = A∩B
print(A.union(B) == B.union(A))
print(A.intersection(B) == B.intersection(A))

#Associative Property
#Union example: (A∪B)∪C = A∪(B∪C)
#Intersection example: (A∩B)∩C = A∩(B∩C)
C = {5,6}
print(A.union(B).union(C) == A.union(B.union(C)))
print(A.intersection(B).intersection(C) == A.intersection(B.intersection(C)))

#Distributive Property
#Union example: A∪(B∩C) = (A∪B)∩(A∪C)
#Intersection example: A∩(B∪C) = (A∩B)∪(A∩C)
print(A.union(B.intersection(C)) == A.union(B).intersection(A.union(C)))
print(A.intersection(B.union(C)) == A.intersection(B.union(A.intersection(C))))
 
#Identity Law
#idempotent Law

## 2.2 and 24 Set operations, Sequences and Summations