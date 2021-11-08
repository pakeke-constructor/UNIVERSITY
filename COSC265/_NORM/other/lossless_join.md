
# lossless join


When you convert a relation to a higher normal form,
you need to split tables up.

    ( See nat_join.png )

Decomposition is lossy if    R1 ⋈ R2 ⊃ R
(Because there is redundant data.)

Decomposition is lossless if    R1 ⋈ R2 = R



# check:
__example__:
Lets say we have relation  R,
    and we decompose it into  R1  and  R2.


Union of Attributes of R1 and R2 must be equal to attribute of R. 
Each attribute of R must be either in R1 or in R2.

Intersection of Attributes of R1 and R2 must not be NULL.

Common attribute must be a key for at least one relation (R1 or R2)

