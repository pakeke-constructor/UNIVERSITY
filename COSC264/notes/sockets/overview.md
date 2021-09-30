

# sockets

Sockets are two-way connections. You cannot have a 3-way socket connection,
so example. It is only ever 2 way.

There can be multiple sockets on the same port.
(See connections.md)

## TYPES:
The types of sockets can either be UDP/TCP or IP sockets.
(There are other types too, but I won't go over them.)


IP sockets (aka Raw sockets) are literally a raw interface 
to OSI layer 3.
No error checking is done, no TCP/UDP headers are generated.

TCP/UDP sockets are what you should use normally. Normal headers
are generated and everything is nice and clean :)


### API:
<NOTE:: from here on out, `sobj` refers to a socket object.>

# bind( (IP, port) )
Connects a SERVER socket object to a local IP and port.
Client sockets use "connect" to register a connection to a server,
server sockets use "bind" to register themselves on their own network.
To get private computer IP see *socket.gethostbyname()*.
>> If you only want connections from LAN you'd go with your computer's IP,
>> but if you want connections from anywhere you'd use 0.0.0.0 or your modem's IP
    >> (Note that modems have a public IP, modems ARE NOT ROUTERS!)

#  listen( max = 10000 )
Opens `sobj` to incoming connections. (i.e. Allows `accept` function to be called.)
If greater than "MAX" connections are made, sobj will stop listening.
> NOTE::: This is usually only used when `sobj` is acting as a server!

# accept( )
Blocks python interpreter until a client connects, unless a timeout is specified.
(Specify a timeout with socket.settimeout( ) )
returns *( socket_obj, ( host_addr, port ))*
>> NOTE: if sobj.listen() hasn't been called, `accept` won't be able to be called!


# connect( address )
Connects the socket to a remote address. 
This is mainly used client-side.

## connect( (host, port) )
Same as `connect`, but for IP sockets.

# connect_ex()


# send( bytes )
send bytes over to the other socket connected


# recv()


# close()
Frees socket