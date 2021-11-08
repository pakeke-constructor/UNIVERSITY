
# B+ Tree

A variant on the B-Tree.
Used in filesystems and databasing, because its faster.


### Whats the difference?

_Main differences:_

B Trees have values at the intermediate nodes.
    Which means that as your traverse the tree, you must do an == check,
    AND a >= check.

B+ Trees don't have values at the intermediate nodes, and store all their values
in leaf nodes.
    - thus, only a >= check needs to be done.
       when you get to the base of the tree, you will have your value.


-----------------------

B+ Trees:
Leaf nodes stored as structured link list


