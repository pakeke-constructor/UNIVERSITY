
# context free grammar


Context free grammar is a way to describe string patterns.

Its done recursively.
For example:

###    A  ->  a | aA
A CFG that matches an arbitrarily long sequence of a's

###    X  ->  yXz | yz
A CFG that matches { y^n z^n  :  n integer }
*(i.e. `n` y's followed by `n` z's)*



More complex example:

###    S  ->   (S) | SS |  *e
Where `*e` is the empty string.
This pattern matches all strings with only brackets,
that have matching open and close brackets.
EG:
- accepted:
()
(())
(())()()

- not accepted:
'ekjfdf'
())
())(




