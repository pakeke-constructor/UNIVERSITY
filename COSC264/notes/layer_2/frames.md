
# Frames

##  Think of a frame as a container for a network packet.
Usually we are talking about Ethernet frames.

Frames are at OSI layer 2, whereas IP packets are layer 3.
TCP / UDP packets are layer 4!!!!


In short, here is the hierachy:


<Ethernet_frame/header>  (used by everyone) contains:
    <IP_header>  (Used by ISP) contains:
        <TCP_or_UDP_header> contains:
            (data)

<end_Ethernet_header>

