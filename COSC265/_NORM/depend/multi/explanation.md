

# Explanation of MVDs:

MVDs are bad, they shouldn't exist in a database.

EXAMPLE:

  id  |  course  |  name
---------------------------
   1  |   cosc   |  bob
   1  |   math   |  bob
   2  |   cosc   |  james
   3  |   math   |  steve
   3  |   phys   |  steve

Here is an example, where  
_id_  -->-->  _course_.

In this example, space is being wasted, because
_id_ ---> _name_, and the name is being repeated.
This wastes space in the database! 

Therefore, MVDs are bad.


#  A better way to do it would be to have 2 tables:

id  |  course
-------------
 1  |  cosc
 1  |  math
 2  |  cosc
 3  |  math
 3  |  phys

id  |  name
-------------
 1  |   bob 
 2  |   james
 3  |   steve


Although the _id_ is repeated in this case, it still saves space,
as strings take up a lot of space compared to _id_'s. 





