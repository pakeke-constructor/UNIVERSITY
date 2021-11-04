

# functional dependency basics:

https://www.geeksforgeeks.org/types-of-functional-dependencies-in-dbms/


Example:


     X     --->     Y

(determinant)   (dependent)


This means that each _X_ can determine a value of _Y_ in a table.
(_X_ and _Y_ may be multiple attributes)

X ---> Y  does NOT mean X computes Y!!!!



## other syntax:
AB -> C  [A and B together determine C]
BC -> D  [B and C together determine D]



# Example:

  X  |   Y   |  Z  
--------------------
  1  |  foo  |  1
  3  |  fes  |  2
  6  |  foo  |  3
 12  |  foo  |  1
  4  |  sdk  |  3
  1  |  foo  | 4



In this example, each value of _X_ maps to ONE DISTINCT
value of _Y_ in the table.
Also, _X_ maps to ONE DISTINCT value of _Z_.

This means that      X ---> Y,
        and also    X ---> Z.

We can write this as   X ---> {Y, Z}


## quick note:
Due to this, it also means that
{X, Y} ---> Z
and 
{X, Z} ---> Y, 
however these are weaker statements than   X ---> {Y, Z}.









### Whats not allowed:
An FD cannot map to multiple values.
For example:

  X  |   Y   
--------------
  1  |  foo  
  3  |  fes  
  6  |  foo 
  1  |  bar

X  --->  Y   IS NOT TRUE HERE!!!
This is because _X = 1_ maps to  "bar" and "foo".

Likewise,  Y  --->  X   is not true, because
_Y = foo_ maps to  1 and 6.
It needs to 





