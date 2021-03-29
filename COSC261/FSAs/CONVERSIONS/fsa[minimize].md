
# TODO

Minimize FSA.

You have already written a python script on this
but its best to be able to do this stuff by hand.

This video is good:
https://www.youtube.com/watch?v=0XaGAkY09Wc&ab_channel=NesoAcademy


## ALGO:

#### For states { A B C D }
#### Make a grid:

    A | B | C | D
A |---|---|---|---|
B |   |---|---|---|
C |   |   |---|---|
D |   |   |   |---|   


#### Mark every pair that contains ONE final state.
(eg, B is final state:)

    A | B | C | D
A |---|XXX|---|---|
B |XXX|---|XXX|XXX|
C |   |XXX|---|---|
D |   |XXX|   |---|

For each state pair {<X>, <Y>}:
    if the pair { δ(<X>, a), δ(<Y>, a) }  is marked
    for any input a, then mark (<X>, <Y>).
        NOTE THAT `--` does not count as marked!!!

- Repeat this process until there are no more minimizations.


    A | B | C | D
A |---|XXX|---|---|
B |XXX|XXX|XXX|XXX|
C |XXX|XXX|---|---|
D |XXX|XXX|   |---|

Aha, {D, C} is a pair left over!
this means {D, C} must be minimized.
