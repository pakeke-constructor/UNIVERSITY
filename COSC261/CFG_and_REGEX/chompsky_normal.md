

# Chomsky normal form (CNF):
CNF is a CFG where the rules have a length limit of 2 on the right.
Its basically a CFG where every rule is of the form:

A -> BC
or
A -> a
where a is any terminating symbol.


####
## Conversion from CFG to CNF:
####
1. Eliminate ε-productions of the form A -> ε. (ENSURE TO REPLACE APPROPRIATELY!!!)
    i.e:
    A -> ε|AB|AC  ====>>>   A -> AB|AC|B|C

2. If  A -> B, replace all A with B.

3. Eliminate anything like W -> W.

4. Other than that, just use common sense to iterate down.



