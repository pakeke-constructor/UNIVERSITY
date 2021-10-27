
# TCP HANDSHAKE.

Lets say A wants to connect to B.

```py

A ----> B   SYN     (request to connect)

A <---- B   SYN_ACK   (acknowledgement of SYN.)
    # If this ios 

A ----> B   ACK      (acknowledgement of SYN-ACK.)

```

*How can A be sure that the ACK packet has been recieved?*

Since wifi channels are very reliable,
If the initial SYN packet was recieved by B, A can be very sure that
they can send another packet that will be recieved reliably.

Also, there is barely any time between sending the SYN and sending the ACK 
(less than a second.) 
So it is unlikely that the connection will fail in that short a time period.


