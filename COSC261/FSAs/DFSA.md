
# What are DFSA's?
(Deterministic Finite state automata)

a FSA is a list of states, where each symbol input to that state
causes a translation to another state.
This allows processing of big strings. 

Each DFSA state must have exactly one output for every symbol in the alphabet.
(Note that the output can be the same for 2 symbols)


##  FSA is a structure:

```py


M = {
    Q    : 'the states of M'
   sigma : 'the alphabet'
   delta : Q x <sigma>  :  'the translation function'
    q0   : 'the start state. (q0 e Q)'
    F    : 'a set of accepting states. F c= Q'
}

```



#  A DFSA can be given a translation table `delta`:

delta 

    q1  q2  q3
  +-------------
0 | q2  q3  q1  
1 | q1  q2  q1
  -------------

An example of a DFSA table across the alphabet <sigma> = {0, 1}

