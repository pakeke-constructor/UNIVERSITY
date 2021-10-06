

GROUP BY is used to group data based on attribute equality.

For example, lets say we wanted to count the number of people with
the first name starting with "S":

```sql

SELECT p.name, COUNT(*) FROM Person p
GROUP BY p.name
HAVING p.name LIKE 'S%';

```
EXAMPLE OUTPUT:
```
Sam 110
Sean 42
Synthia 1
Samira 2
```






Also note that aggregate functions can be used in the `HAVING` statement:

```sql

SELECT p.name, COUNT(*) FROM Person p
GROUP BY p.name
HAVING COUNT(*) >= 50

```
This query lists the names and name counts of all names
where there are 10 or more people with the same name:

EXAMPLE OUTPUT:
```
Sam 110
John 74
Tim 51
Kate 65
```


