
# Internet protocol

IP packets are usually most useful to the Internet Service Providers (ISPs).

IPv4 and IPv6 headers hold the *actual IP addresses*.

This means that they are vital for routing the actual packets




## v6 and v4
There are two protocols, IPv4 and IPv6. (See the headers.)

IPv4 contains way less public IPs, but has built in error checking.

IPv6 has many more addresses, but no error checking. This was done
because it would be faster; <see_below.>
Also, IPv6 cannot be multiplexed; the packet headers are too big and it would
be very inefficient. You'll need to send multiple IP packets instead.

> Why no error checking for ipv6?
Ethernet frames do error checking on IPv6 already.

Also, when hop count is decreased, the checksum must be recalculated. This is
very costly time wise! (Especially since IPv6 headers are big.)
Therefore, no error checking for ipv6





### hop limits / time to live (TTL)
Both v6 and v4 protocols have set limits on how many "hops" between routers
are possible before the packet should be discarded.
(called *Hop limit* in ipv6,  called *Time to live* in ipv4.  )
This is to prevent packets from cycling around the network forever.













