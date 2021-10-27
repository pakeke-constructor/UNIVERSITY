
# routers 

    ( NOT TO BE CONFUSED WITH A MODEM! )


Routers hold a list of private IPs, and recieve
packets.

Routers can route to any public IP, and can route
to and from and private IP it controls.


Routers can allow for multiple connections across multiple
devices.




## Routing table:

__A routing table must have these three information fields:__

- Network identifier: 
    (The destination subnet and the netmask)

- Metric:
    (The relative computational/time cost of the network pathway)

- Next hop:
  - The next hop, or gateway, is the address of the next station
     to which the packet is to be sent.
    (The router knows this because )




A Home routing table could look like this:


Dest       |  Net mask    |  Gateway    |  Interface  |  Metric
=================================================================
0.0.0.0    | 0 0 0 0      | 192.168.0.1 | 192.168.0.5 | 10      
127.0.0.0  | 255 0 0 0    | 127.0.0.1   | 127.0.0.1   |  1



Fields:

*Network identifier*  ::  Dest and Net mask; could be written as 
                                127.0.0.0/8   (8 = first 8 bits.)

*Gateway*   ::   Contains information for the next hop.
        In this case, send data to 127.0.0.1. This is probably a
            private address managed by the ISP.

*Interface*   ::  Describes what locally available device is
    responsible for reaching the gateway.
    (Interface is just your devices private IP on the home network.)



