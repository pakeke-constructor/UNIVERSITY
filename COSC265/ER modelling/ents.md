
# Entities in DBMS

Each "entity" represents a collection of attributes.  (Data)
think like a C struct.

Each ent should also be able to be uniquely identified,
through one or more of it's attributes   (<see key_attr.md>)

## "weak ents"
If an entity cannot be uniquely without outside help, then it is a **weak entity**.

Weak ents must have partial key attributes,
and weak ents must have an "identifying relationship"



