

## All SQL Queries follow the same format:
```sql

SELECT attr [, attr ...] 
FROM  SomeTable
WHERE [optional condition];
/* In the WHERE clause, you can access attributes of each individual
SomeTable object.
For example:  WHERE SomeTable.foo = 'Bar'

In this case, SomeTable refers not to the actual table, but rather to
each and every instance inside SomeTable.
*/
```
And this will basically push SQL's data to your own program,
(is implementation dependent.)


## More advanced format:
```SQL 


SELECT attr [, attr]* 
FROM  SomeTable
WHERE condition   /* WHERE, GROUP BY, HAVING,and ORDER BY are optional. */
GROUP BY attr [, attr]* 
HAVING condition /* same as WHERE, but "aggregate functions" are allowed. */
ORDER BY attr

```
