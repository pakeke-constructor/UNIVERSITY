
# 2s complement

A way to represent signed integers:


We can represent a signed int as a regular unsigned integer, but we keep
the first bit as a "sign" bit.

I.e.
```py

01010

```
The first zero in this case tells us whether the number is negative or not.

If it is zero, then the number is the same as it's unsigned counterpart.

If it IS zero, however,
Then take the unsigned number and add it to the max negative value it can take.



# EXAMPLE:

Number,  Binary val
----------
0  |	000
1  |	001
2  |	010
3  |	011
−4 |	100
−3 |	101
−2 |	110
−1 |	111



