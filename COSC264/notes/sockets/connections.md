

### How are socket connections identified?

TCP/UDP Socket connections are uniquely identified by the OS
by the following 5-tuple:

    (local-IP, local-port, remote-IP, remote-port, protocol).
If any element in the tuple is different,
then this is a completely independent connection.
(Note that this is the reason `remote-IP` and `remote-port` must be stored
in the UDP/TCP header)

See this SO answer: (the higher rated one) https://stackoverflow.com/questions/11129212/tcp-can-two-different-sockets-share-a-port

This also means that UDP/TCP sockets can share ports, because they are not
identified by ports- but rather by the above tuple.



# Lower level connections:
Lower level connections (EG, IPv4 packets) that don't use ports
must be identified by the tuple:

    (local-IP, remote-IP)
Which means you cannot have multiple connections to the same remote IP.
