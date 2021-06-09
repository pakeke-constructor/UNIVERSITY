
# Pushdown automata

Pushdown automata are same as DFA's, except they have an infinite stack also.
Stack operations: (<push>, <pop>, <do nothing>)
Note that popped values are not read.

There is also a <peek> operation that is used seperately.

The stack does not take the regular alphabet- it has an alphabet of it's own.
Most notably is the `_` symbol which represents an empty stack position



## transitions:
Each transition is marked by a tuple, like this:

####  x, A/B
-- <input>:
`x` is the terminal symbol read at the current point in the string.
`A` is the top stack value. (peeked from top)
-- <operation>:
`B` is a stack operation

When a transition is to be made, both the Stack symbol AND the current
terminal symbol are read. The transition input is BOTH of these things.

#### When the transition is made:
- Alike DFA, go onto next symbol
- Execute the stack operation `B`.






An input will only be accepted if the stack is empty, AND it is in an accept state.

