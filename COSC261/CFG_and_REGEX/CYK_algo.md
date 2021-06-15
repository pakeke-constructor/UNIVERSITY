

### Parsing a string with CFG

> NOTE:
This algo only works for languages in Chompsky Normal form!!!


https://www.youtube.com/watch?v=VTH1k-xiswM&ab_channel=EducationAboutStuff

# Algorithm:
EG: rules:


K = XW
W = ZZ
X = YX|a|YZ
Y = Za|XZ
Z = Xb

now lets parse the string: <abb>

Make a triangle table, with base the size of the string:
<abb>:
```
    _____
  __|   |__
__|   |   |__
|   |   |   |
=============
| a | b | b |
```

- List all the rules in the bottom row that contain
    the initial character.

=> X and Y contain a.
=> Z contains b.

```
    _____
  __|   |__
__|   |   |__
|X,Y| Z | Z |
=============
| a | b | b |
```


#### Main step:
Now, list all the rules in the next row
that can contain the *combined* grammar rules.
(get combined grammar rules by taking set product.)

| a | b | ===> |X,Y| Z |
     set prod  X,Y x Z    -->
ab:   XZ, YZ
    what contains XZ, what contains YZ?
        aha!   X contains YZ.
        Y contains XZ.
    mark X,Y in box, because it contains an elem from the product.


bb:   Z x Z
bb:   ZZ
    what contains ZZ?
    aha! W contains ZZ.
    mark W in box.


```
    _____
  __|   |__
__|X,Y| W |__
|X,Y| Z | Z |
=============
| a | b | b |
```

repeat the above step.

| X,Y | W | ==>   XW, YW
well, K contains XW, so final pattern matched is K.

```
    _____
  __| K |__
__| X | W |__
|X,Y| Z | Z |
=============
| a | b | b |
```


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
