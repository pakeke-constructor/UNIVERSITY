
# Pushdown automata

Pushdown automata are same as NFA's, except they have an infinite stack also.

The stack does not take the regular alphabet- it has an alphabet of it's own.
Most notably is the `_` symbol which represents an empty stack position

    (Note::: Since PDA's are similar to NFA's, they can have multiple
    transitions for the same stack symbol or read symbol. This can be
    used to emulate an `or` in CFG's, like  A -> B | C. )


# transitions:

####  x, Pop / Push

`x` is the terminal symbol read at the current point in the string.

`Push` is the symbol to be pushed
`Pop` is the symbol to be popped

    (Every single iteration, stack symbols are pushed and popped.)

>>>> example:
  >>>>        a, ε/T
a reads the symbol `a` from the string.
`T` is popped off the stack.
`ε` is pushed onto the stack.


When a transition is to be made, both the Stack symbol AND the current
terminal symbol are read. The transition input is BOTH of these things.

#### When the transition is made:
- Alike DFA, go onto next symbol
- Execute the stack operation `B`.


An input will only be accepted if the stack is empty, AND it is in an accept state.






### Context free grammar to PDA:
See <CFG_to_PDA.png>.




