
# attribute closures

The closure of a set of attributes X is the set of
 attributes that can be functionally determined from X.
 
 The closure of X is denoted as {X}+.

 For multiple attributes, the closure can be denoted
 as:  {X,Y}+




# algorithm ::
Add elements of attribute set to the result set.

Recursively add elements to the result set which 
can be functionally determined from the elements of the result set.







## EXAMPLE
Lets say we want to find the attribute closure of A.

R(A, B, C, D, E)

A ---> B

B ---> C

A, C ---> E

straight away, we can see A ---> B. So we add _B_ to the attribute
closure set.


{A}+ = {B, ...} _maybe there are others!_

Now, we repeat the process recursively:

C can be obtained from {A,B}, because B--->C.

{A}+ = {B, C, ...} _maybe others!_

E can be obtained from {A,B,C}, because  A,C ---> E.

{A}+ = {B, C, E}
_and thats it._






