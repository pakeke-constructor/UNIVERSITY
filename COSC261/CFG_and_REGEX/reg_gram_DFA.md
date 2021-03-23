
### *
Regular grammars are one of the form:
### *
(Where <e> is the empty string)

A -> <e>

A -> aB

A -> a


And where `a` is a terminal symbol (alphabet element)
and B is an array of symbols



# CONVERT REGULAR GRAMMAR TO DFA:
## Algorithm:
*Notes:*
lowercase letter denotes primitive symbol
Uppercase denotes CFG variable
--<x>--> denotes DFA transition with `x`.

#### How to do algorithm

- Create a state for each variable
    i.e. { A, B, C }

- Convert each production rule into a transition
    - If rule is:    A -> xB,
    Make an edge A --<x>-> B, with transition char `x`.
    
    - if rule is:    A -> xyB, 
        make new temp state, A_1
        Make A --<x>--> A_1 --<y>--> B

    - if rule is:
        A -> a
        This means that A is a final state.
        do:
            A --<a>--> <final_state>


