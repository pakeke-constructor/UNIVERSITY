

# Chomsky normal form:
this is a CFG where every rule is of the form:

A -> BC
or
A -> a
where a is any terminating symbol.

### IMPORTANT:
In chomsky normal form, rules can have multiple matches.
i.e. this is allowed:

A -> BC
A -> a

This is the same as writing:
A -> a | BC
except we dont use this syntax sugar in chomsky normal form

