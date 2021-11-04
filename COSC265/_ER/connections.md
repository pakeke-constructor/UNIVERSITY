

<Amazing_article:  https://www.tutorialspoint.com/dbms/er_diagram_representation.htm >



.
             __
            /  \
      1    /    \    N
Ent ------| name |======== Ent here too
           \    /
            \  /
             --

Ents can be related with a line and a diamond "relation".
(see relations.md)
The lines connecting them are called <Connections>.

# CONNECTIONS


### participation  ( === or --- )
#### ( see connections.png )
Connections can either be *total* or *partial* participation,
shown by the look of the line.

total participation: double line
====================
Every entity is involved in the relationship


partial participation: single line
--------------------
Not all entities are involved in the relationship



### cardinality
Cardinality determines how many entities are involved in a relationship

There are *1 to 1* relationships, 1 to 2 relationships, 2 to 3, 
and in general, there are   *N to M*  relationships, where N,M ∈ {N+}

If there are 2 ents in a relationship, it is called a *binary* relationship.
If there are 3 ents in a relationship, it is called a *ternary* relationship.
If there are N ents, it is called "N-ary"


For example, a relationship relating passengers on a plane to the aeroplane
      would look like:

Passenger -------- < flies on > ---------- Aeroplane
             N                       1

This relationship is a "one to many" relationship.
( *1 to N* )

Note the "participation" of the lines as well. Aeroplanes may not have any passengers,
and a passenger may not fly on the aeroplane, because they miss their flight for example.





