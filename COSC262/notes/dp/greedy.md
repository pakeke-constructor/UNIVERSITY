
## Greedy algorithms

Greedy algorithms are algorithms that take the best solution at every step.

Example:
greedy coin match algorithm:

```py
def coins(val, coins):
    take away the highest value coin,
    until no more value.

    repeat for smaller coins, until no coins left.
```

For the coin matching algorithm, greedy algorithms can yield incorrect solutions
if there are coins that have different prime factors.

EG:

coins(60, [50,20,1]) yields incorrect answer with greedy
