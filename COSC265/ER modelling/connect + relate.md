
# Connections and relations

<Amazing_article:  https://www.tutorialspoint.com/dbms/er_diagram_representation.htm >



# RELATIONS
Relations are represented by a diamond symbol.
             __
            /  \
           /    \
Ent ------| name |======== Ent here too
           \    /
            \  /
             --



The lines connecting to the relation are called:
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



For example, a relationship relating passengers on a plane to the aeroplane
      would look like:

Passenger -------- < flies on > ---------- Aeroplane
             N                       1

This relationship is a "one to many" relationship.
( *1 to N* )

Note the "participation" of the lines as well. Aeroplanes may not have any passengers,
and a passenger may not fly on the aeroplane, because they miss their flight for example.





