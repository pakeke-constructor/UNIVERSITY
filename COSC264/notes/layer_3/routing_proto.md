

## Routing protocols.

Some of them work in a decentralized environment.



### Types:

  __PROTOCOL__          __ALGORITHM__
      RIP      >>>   Bellman-Ford DV algorithm    (Decentralized)
      OSFP     >>>   Dijkstra's Algorithm       (Not Decentralized!)
      BGP      >>>   Bellman-Ford DV algorithm    (Decentralized)


### How does centralized stuff work?
_Answer_:
    Use __Link state routing.__       
    Link state routing floods the entire network with all
    the connection information, so each network node knows
    what the entire network looks like.
_Answer 2_: 
    OSFP could also be used on a private network!
    For example, the Uni could use OSFP to route their
    traffic. In this case, there could be one computer that
    oversees the entire network state.
    


Static/dynamic routing protocol:
    Static = routes dont change much.
    Dynamic = routes change a lot, i.e. high traffic causes change.






#### Load sensitivity
Each algorithm must have a link cost.

    Load sensitivity:
    Whether or not the link costs varies with respect to the current
    data load that is being sent through.

All the internet routing protocols are load-insensitive,
because sending data changes the cost and its too inconsist

