

# socket()
Creates a socket object

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

# sobj. bind( (IP, port) )
Binds a socket object to an IP and port.
To get private computer IP see *socket.gethostbyname()*.
>> If you only want connections from LAN you'd go with your computer's IP,
>> but if you want connections from anywhere you'd use 0.0.0.0 or your modem's IP


# sobj. listen( max = 10000 )
Opens `sobj` to incoming connections.
If greater than "MAX" connections are made,
    sobj will stop listening.
>NOTE::: This is usually only used when `sobj` is acting as a server!

# accept()
Blocks python interpreter until a client connects,
(unless a timeout is specified.)
returns *( socket_obj, ( host_addr, port ))*

# connect( address )
Connects the socket to a remote address. 
## connect( (host, port) )

# connect_ex()

# send()

# recv()

# close()
