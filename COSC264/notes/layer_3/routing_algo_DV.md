

# Bellman Ford (Distance vector) algorithm
^^^ Offers a pathfinding solution for a decentralized network.

This algorithm is actually really smart and cool.




```py
Let:
 cost(a,b) be the path cost between a,b where a,b are attached.


Let:
def d(x,y) = ''' cheapest path from x -> y.   
                (Even if x,y arent directly attached!) '''

Thus:
def d(x,y) = min( c(x,v) + d(v,y) )  for all nodes v attached to x

```


### How this works Distributed:
Each node keeps a table of Distance Vectors:
    d(x,y) = DISTANCE

Whenever a node's connection changes, notify neighbours.
    The neighbours will notify the rest of the network 
    if there is a significant change

_pseudocode is below._


### Count to infinity problem:
https://www.ques10.com/p/3796/what-is-count-to-infinity-problem-in-distance-vect/

This happens when the nodes rely on bad data that was only true
    in the past.  (Same as a routing loop.)

Key words to google:  Poisoned reverse

The solution that is used in `RIP` is the maximum cost of a path
is limited to 15.




#### PSEUDOCODE:
```py
# let `self` be the current node that is doing the algo.

# let `d` be a function / table giving best cost of any two nodes.

# Initialize:
for v in neighbours:
    d(self, v) = cost(self, v) or inf

for w in neighbours:
    for dd in all_destinations:
        if dd is not self:
            d(w, dd) = inf

while 1:
    wait until link cost change from neighbour:

    for dest in all_destinations:
        for v in neighbours:
            d(x, dest) = min( cost(x, v) + d(v, dest) )

        if destination distance has changed:
            send new DV d(x, dest) to neighbours.
```

