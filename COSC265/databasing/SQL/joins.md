
## Joins
There are different types of joins.

Joining allows you to access multiple different tables in one SELECT
statement.

"Joins" can take the place of a table name in a select statement.
I.e:
```sql
SELECT * FROM tab1;
SELECT * FROM (tab1 JOIN tab2);
```

# TYPES:

```sql
-- Inner join joins everything in a table provided the condition
-- is met.
PetOwner INNER JOIN Pet ON [condition]; 
-- For example, if we wanted to list all pet names and owner names:

SELECT PetOwner.name, Pet.name FROM
    (PetOwner INNER JOIN PET on PetOwner.id = Pet.id)




-- Left join 




```

