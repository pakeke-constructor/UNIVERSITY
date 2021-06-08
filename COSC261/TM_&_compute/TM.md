
# Turing machines
(aka, TMs.)

Turing machines are very similar to DFAs, except they have memory.

TMs have an infinite block of memory called the "Tape", which can
store any symbol in it's defined alphabet alongside the blank symbol _.

### The starting memory of the TM will be the string in question.
For example:
"1001001"
The tape starts off as:

 |
 V
[1][0][0][1][0][0][1]

(with tape pointer in start char position)


### Each TM path will have a label:    a / b, R

The a is read symbol
The b is write symbol
and R stands for move pointer right. (L stands for go left; N for no move.)


The TM reads a symbol each iteration. When it reads it, it goes to 
that path.
EG: if it read symbol X, and the branch was (X _ _), it would go to that path.

## Finishing::
If a turing machine finishes 

