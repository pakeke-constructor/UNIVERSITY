

# Non-deterministic finite state automata


These are the same as FSAs, except states
can have more or less than 1 output per symbol.

- If a state has more than one output for a symbol, 
  the NDFSA will go to either of the branches

- If a state has no output for a symbol,
  the NDFSA will stop execution.


# passing / truthyness:
If a passing state is reachable for a string,
the string is passed.
(Even if there is only 1 path that leads to the passing state)

