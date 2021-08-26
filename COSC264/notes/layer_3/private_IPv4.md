

## Priv/public addresses
since ipv4 total addresses is only uint32, IPv4 ips can get exhausted easily.

> To counter this, there are private IPs and public IPs.
*Note that private IPs can have many layers of nesting See NAT_2.png.*

(This is what ISPs do. For example, an ISP could assign a public IP to a city,
a private IP to each suburb in the city, and each house router has a nested private IP
inside of that.)

Private IPs lie in range:  10.0.0.0  —  10.255.255.255
                           172.16.0.0  — 172.31.255.255
                           192.168.0.0  —  192.168.255.255

Public IPs are any IP that isnt a private IP.



### In total, there are 17,891,328 private IPv4 IPs.

