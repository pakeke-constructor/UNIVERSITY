
# LIKE operator SQL


Like is used for string pattern matching,
in WHERE clauses.

(See: https://www.w3schools.com/sql/sql_like.asp)
```sql

    % /* represents 0 or more characters */

    _ /* represents one single character */

```






# examples:

```sql
WHERE CustomerName LIKE 'a%'
/*	Finds any values that start with "a" */

WHERE CustomerName LIKE '%or%'
/* Finds any values that have "or" in any position */

WHERE CustomerName LIKE '_r%'
/*	Finds any values that have "r" in the second position */

WHERE CustomerName LIKE 'a__%'
/* Finds any values that start with "a" and are at least 3 characters in length */

WHERE ContactName LIKE 'a%o'
/* Finds any values that start with "a" and ends with "o" */
```