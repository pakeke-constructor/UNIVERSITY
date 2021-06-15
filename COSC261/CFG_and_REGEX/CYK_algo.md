

### Parsing a string with CFG

> NOTE:
This algo only works for languages in Chompsky Normal form!!!


https://www.youtube.com/watch?v=VTH1k-xiswM&ab_channel=EducationAboutStuff


The CYK algorithm utilizes dynamic programming.
You just gotta ensure you are constantly looking
back at the string, and list the substrings:


### Lets match the string,  abc

A -> a
B -> b
C -> c | BC
Z -> AC

start off with empty tabl like this:
     ___
    |   |    substr size 3
  |   |   |     substrs size 2
|   |   |   |      substrs size 1 
-------------
| a | b | c |      terminals


Now for the strings `a, b, c`,
we gotta find all the rules that matches our substrings of length 1:
Aha! its   A,B,C
.
     ___
    |   |
  |   |   |
| A | B | C |
-------------
| a | b | c |

Now is hard bit: for each *substring,* ab, bc,
we find what matches it:
substrings:
ab --> AB
bc --> BC

We match `C` for `bc`, 
and empty set for `ab`
.
     ___
    |   |
  | 0 | C |
| A | B | C |
-------------
| a | b | c |


Now lets list all our substring of length 3:
a bc
ab c   
>>>>> (note that since it's in Chompsky norm form, there must only be 2 components!!!)

aha, we have a matching for `bc`: it is  `C`.
And `a` is matched by `A`.
Is there an `AC` matching?
!!!! Yes there is!! Z -> AC

.
     ___
    | Z |
  | 0 | C |
| A | B | C |
-------------
| a | b | c |


and we are done.
wowza, I really messed up my notes previously didnt I




#
#
#
#
#
#
#



### PSEUDOCODE
```lua
let the input be a string I consisting of n characters: a1 ... an.
let the grammar contain r nonterminal symbols R1 ... Rr, with start symbol R1.
let P[n,n,r] be an array of booleans. Initialize all elements of P to false.

for each s = 1 to n
    for each unit production Rv → as
        set P[1,s,v] = true

for each l = 2 to n -- Length of span
    for each s = 1 to n-l+1 -- Start of span
        for each p = 1 to l-1 -- Partition of span
            for each production Ra    → Rb Rc
                if P[p,s,b] and P[l-p,s+p,c] then set P[l,s,a] = true

if P[n,1,1] is true then
    I is member of language
else
    I is not member of language
```
