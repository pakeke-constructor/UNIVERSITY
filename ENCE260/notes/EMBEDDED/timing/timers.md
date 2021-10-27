
# Timers

We can record the time of the clock in real time,
and have the clock use a synchronous counter to track the time.

Thus, the time is given by the formula:

```sql
Time = Count * Period,
```

Where `Count` is the current count, and `Period` is the time taken to complete
a singular clock cycle.



NOTE that in this case, the clock must be very very consistent!

This is why special timing components are often used, instead of baking the timer
directly into the microcontroller's clock.
