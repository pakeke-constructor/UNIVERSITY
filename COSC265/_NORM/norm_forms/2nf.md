
# 2nd normal form
[requires_1nf]


## 2nf:
requires that tables have 1 primary key,
i.e. primary key is not comprised of multiple attributes.

IN OTHER WORDS:
There are no FDs that can be derived by reflexivity


# Conversion::
Write out the FDs, 
and check for reflexivity.

Remove reflexivity if you can.






## EXAMPLE :

Lets say we have this database:
```PY

STUDENT_NO        COURSE_ID         COURSE_FEE
1                     C1                  1000
2                     C2                  1500
1                     C4                  2000
4                     C3                  1000
4                     C1                  1000
2                     C5                  2000
```

There is a composite primary key here!!
The primary key is {STUD_NO, COURSE_NO}.

This is bad, as we cannot access data easily.
Therefore we decompose into multiple tables such that theres only 1 primary key.
```py
COURSE_ID ---> COURSE_FEE
{STUDENT_NO, COURSE_ID} ---> COURSE_FEE ## This is a weaker form of the above!!
```
^^^^ data redundancy here.

We can convert it as so:
```py
       Table_1 ()                                  
STUDENT_NO      COURSE_NO         
1                 C1               
2                 C2              
1                 C4         
4                 C3               
4                 C1               
2                 C5            

        Table_2   ()
COURSE_NO                COURSE_FEE     
C1                        1000
C2                        1500
C3                        1000
C5                        2000  
```

Now, the FDs are as so:

COURSE_NO  --->  COURSE_FEE

We have removed the redundant FD,
via the Reflexivity rule.


