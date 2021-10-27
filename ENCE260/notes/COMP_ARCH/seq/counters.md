
# Ripple counters

A register will automatically increment itself at the rise of the CPU clock.

*How does a register automatically increment itself?*
Note that each component in the CPU, registers, transistors, EVERYTHING,
have a "supply current" flowing through them that provides energy to
keep the circuit going.
This is called the "clock".


Ripple counters are used at the heart of the CPU in order to count the current
clock position.

A diagram can be seen at ripple_ctr.png




### PROBLEM:
The issue with ripple counters is that
in order for the whole counter to update, every single flip-flop must update
before the next flip-flop knows whether to update or not.

This is an issue, as it makes ripple counters (relatively) slow.


## SOLUTION:
### Synchronous counter!
Use logic gates to predict the next output for each flip flop.

(This is called a "synchronous counter".)


