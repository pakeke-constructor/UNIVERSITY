

# 3rd normal form


# 3nf:
Requires no FDs that can be derived by transistivity.


## example:
Lets say we have the table:

#  WORKER (id, name, region, country)


with FDs:
id ---> region
region ---> country

Aha, there is a transistive FD here!!
id ---> region!

We can simplify this by putting it into two tables:

#  WORKER (id, name, region)
#  REGION_COUNTR( region, country )

