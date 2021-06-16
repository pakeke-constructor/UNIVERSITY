
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


### Each TM path will have a label:    read / write, M

`M` stands for move. It will either move the instruction pointer
left (L) or right (R), or not move, (N).


The TM reads a symbol each iteration. When it reads it, it goes to 
that path.
EG: if it read symbol X, and the branch was (X _ _), it would go to that path.

## Finishing::
If a turing machine finishes in an accept state, that input is accepted.
else, it is rejected




#### recording TM progress.
The paper will ask you to record the progress of the TM.
Record your progress in this format:

    ( 0 q0 100 )  1/0, R 

This means that the tape looks like this:
    |
    V
[0][1][0][0]
And that the TM is currently at state q0.

1/0, R    is the transition that is made from that state




