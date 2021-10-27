
# CPU caches

When operations are done on data, everything happens
on the registers attached directly to the CPU cache.

On intel i7,
there are three CPU caches:

L1 cache  (closest to CPU, )
L2 cache
L3 cache  (furtherest from CPU, has most memory.)

There is also the RAM.


When you try and access data from memory, the program
will (or SHOULD) first check if the data has already been
loaded into one of the caches.

If it hasn't already been loaded into one of the caches,
it is a "cache miss." <--- these are v. costly!



To avoid lots of cache misses, try and load data in big arrays.
This way, when you access the next object, chances are
it will already be in one of the caches.



