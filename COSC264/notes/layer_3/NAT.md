
# Network address translation

## NAT IS REALLY REALLY COOL :)))) 

NAT works by each router having it's own translation table.
REMEMBER UDP AND TCP:
Each connection is identified uniquely by it's `port` and `ip address`.













### 
# EXAMPLES:
###



__EXAMPLE__:
Lets say we have a router with a public IP.
We want to send a packet to 142.250.66.174  (google.com.)

This shows the entire journey of the packet header,
being sent from our computer  --> google.

(ASSUME THAT OUR ROUTER's IP IS PUBLIC!)

Our TCP header we send to router is:

__|     src port     |     src ip     |     dest port     |     dest IP     |__
            169              computer IP             1000               google IP

>>> Now, the router will allocate it's own port of it's choosing, and change
>>>  the __dest ip__ to it's own public IP address.
>>>  Router allocates src port 100, and changes the ip to its own.

>>> Also, a tuple is added to the translation table:
    (100, router pub IP, 169, computer IP)
>>> (Note that this is a 2 way tuple. In reality, 2 entries will be made- one for incoming, one for outgoing.)

This is what the packet looks like now:

__|     src port     |     src ip     |     dest port     |     dest IP     |__
            100           router public IP          1000                google IP

Now the packet has a destination IP that is in the global IP address space.
So we can send the packet directly to google through our Autonomous System (ISP in this case.)

When google recieves the packet, it DOES NOT KNOW the initial computer IP, 
or the initial port used by the computer; it ONLY KNOWS the port allocated by the router,
and the router's public IP address.

This shows the journey of the packet sent from
google  -->  our computer

__|     src port     |     src ip     |     dest port     |     dest IP     |__
           1000              google IP              100             router public IP

>>> Hits router.
>>> Router looks up translation table and changes fields:
>>> Note the dest port: it is the same as what the computer first said!! Thanks router!

__|     src port     |     src ip     |     dest port     |     dest IP     |__
           1000              google IP               169               computer IP











###
## Multiple layers example:
###

This kind of thing is a basic example, as the router IP is public.

If this were to happen IRL, there would have to be more layers of translation
in order to get to the public IP address realm.

Think of it like chaining.

Imagine our router IP is not public, and is contained inside a larger network that is public:
 EXAMPLE:


__|     src port     |     src ip     |     dest port     |     dest IP     |__
            69          computer private ip          100               google IP

>>> router translation (router is not public.)
>>> tuple added to translation table:
    (69, computer private IP, 100, google IP) 
>>> Router also allocates whatever port they like.

__|     src port     |     src ip     |     dest port     |     dest IP     |__
            674            router private IP          100                google IP

>>> Router has a private IP inside the ISP-deployed subnetwork.
>>> tuple added to translation table:
    (674, router private IP, 100, google IP)
>>> ISP-network gateway router allocates an available port for this router private IP.

__|     src port     |     src ip     |     dest port     |     dest IP     |__
           12955       ISP-network gateway ip        100                google IP

!!!!!                                                          
Google recieves the packet, and sends a response packet!       
Now the return journey begins:                                 
!!!!!                                                          

__|     src port     |     src ip     |     dest port     |     dest IP     |__
            100              google IP              12955         ISP-network gateway IP

>>> Header translation by ISP-network gateway router.

__|     src port     |     src ip     |     dest port     |     dest IP     |__
            100               google IP              674            router private IP

>>> Header translation by router 
>>>     (the router that resides on the private ISP deployed network.)

__|     src port     |     src ip     |     dest port     |     dest IP     |__
            100               google IP               69            computer private IP



##
# question:
# If every public connection is identified by a port and public IP,
# why don't public IP routers run out of ports?
# Ports only go to 0-65535!
###
Answer:

There are many MANY public IPs.  (2**32.)
In New Zealand, ISPs control a whopping 6205440 public IPs.

(See NZ_pub_ips directory for details)

Since Each public IP can contain 65355 distinct connections to the same
    address, you would need to connect 65355 computers to google.com
    on the exact same public IP, which would never happen!

There are too many public IPs, and even if you tried,
the ISP would probably reallocate your traffic to another one of their
public IPs anyway.





__HOLEPUNCHING__:

Holepunching is a similar process, except translation is done on both sides.
Notice in the examples, google did no NAT on their part.
They just recieved the packet and sent it back on their public IP.

In order to set up hole punching, we must have a public IP to set up
the initial connection.

FLOW DIAGRAM:

Let there be a server with public IP: `SERV`.

Computer __A__ with private IP connects to SERV
Computer __B__ with private IP connects to SERV.

SERV does not see A and B's private IPs, but rather sees the public IP
and the port that A and B are using to connect to the internet.


