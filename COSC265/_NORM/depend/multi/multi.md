
# Multi-Valued dependency basics
READ   _NORM/depend/functional/basic.md first!!!

_Every FD is also an MVD,_
_BUT THE CONVERSE IS NOT TRUE!!!_

# MVD:
whats difference between   X ->-> Y    and    X ---> Y ?
An FD is a special case of an MVD where X can map to only
1 value of Y.


Unlike functional dependencies, MVD's are *really bad*,
and are generally a result of bad database design.
_See solving.md for how to resolve MVDs._


#### watch this, it is really really good.
https://youtu.be/OTCuykFHBeA?t=116
####
# Also, check out explanation.md for my hand-written explanation.


# Conditions:
Let there be a table with columns _A B C_.

A  -->-->  B


- For a value _A_, 1 OR MORE values of _B_ exist.

- There must be at least three columns in the table

- B and C must be independent.




