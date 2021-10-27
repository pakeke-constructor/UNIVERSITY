
# Data registers:


There are 3 ports in our example:
B, C, or D.
_.   Let x be B or C or D  ._


## DDRx
The data direction register. (0 or 1)
0 = signals input
1 = signals output

## PORTx    (bidirectional!)
IF DDRx = 1:
Then each register bit gives an output value.
    1 = on, 0 = off.
    (Gives it so some other part of the circuit.)

IF DDRx = 0:
Then each register bit controls the pullup resistor:
    1 = pullup resistor ON,
    0 = pullup resistor OFF.

THE PULLUP RESISTOR NEEDS TO BE CONTROLLED FOR LED MULTIPLEXING!


## PINx
Input value.

