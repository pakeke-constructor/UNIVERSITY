
# UNIQUELY IDENTIFYING ENTS
Ents need to be uniquely identified. We can do this by
assigning them a unique attribute. 
For example, student id is an attribute that uniquely IDs an ent.

    ( This is important, because what if two ents have all the same
    data fields or something? You need a way to uniquely identify.)


# attribute
Just a data field, think like C struct member



## key attribute
A single attribute that uniquely IDs an entity.




## derived attribute
A set of attributes that work together to uniquely ID the entity.
>        For example: if we have date of birth, AGE is a derived attribute.
    
    ( NOTE:: derived attributes take up no space! They are simply composed
    from other non-key attributes.)


# partial key attribute   
The key attribute of a weak entity.

(NOTE THAT THIS ISN'T ENOUGH TO IDENTIFY AN ENTITY; you also need
the identifying relationship too.)




# multivalued attribute
An array of values


