
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


# With top-down derivations, there is leftmost and rightmost derivations.
## (for bottom-up, see CYK algo.) 

Leftmost derivation, means do top-down, and match stuff on the left first.

Rightmost derivation is the same, but on the right.

### NOTE::
You may be dubious doing this top-down because you may need to backtrack.
Trust me- dont worry, just YOLO it. If it is in the exam, the examiner will make it really easy.
trust.

https://www.tutorialspoint.com/automata_theory/context_free_grammar_introduction.htm
https://en.wikipedia.org/wiki/Ambiguous_grammar#Addition_and_subtraction


