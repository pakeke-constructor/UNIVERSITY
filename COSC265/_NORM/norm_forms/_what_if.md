
# What can happen if the table is not normalized?

There can be update anomalies if the table is not normalized.


For example,
lets say we have teachers:


id  |   room   | department
--------------------------
1   | room 1   |  marketing
2   | room 40  |  math
2   | room 40  |  cosc
3   | room 9   |  math
4   | room 63  |  phys


Let say we want to move teacher 2 to room 30.

The database user may update only one row, which will be bad.


