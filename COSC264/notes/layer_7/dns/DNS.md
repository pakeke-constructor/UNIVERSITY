
# DNS (Domain name service)

It is a decentralized  string --> ip  conversion mechanism.




# Every suffix routes to a server.
WHAT HAPPENS WHEN YOU DO   google.com   DNS LOOKUP?


Also note in this example, the .com suffix is owned by Verizon.

the ISP should know where to locate the Verizon server; 
the Verizon lookup server IP/s are hardcoded in by humans.

(Assume the ISP and your computer have done no memoization.)



_Your computer ---> ISP_:
    give me  www.google.com
    
    ISP: Okay


_ISP ---> Verizon server_:   (Autoritive Root Server)
    give me  www.google.com
    
    > Verizon server:  Okay, here, take the lookup server for .com:
        192.26.92.30   (DNS name: c.gtld-servers.net)


_ISP ---> 192.26.92.30_:    (Authoritive TLD Server)
    give me www.google.com
    
    >192.26.92.30: Okay, here:
        142.250.66.206   
    this ^^^^^ is an  Authoritive SLD Server;
    google may want to re-route you.




_ISP_:  Caches verizon lookup ip address
_ISP_:  Caches www.google.com ip address



_ISP ---> Your computer_:
    Here you go:  142.250.66.206


_Your computer_:  Caches www.google.com ip address


