

# Multiplexing

Multiplexing is the act of dividing big bits of data up into multiple
parts so it can be sent over a network better.

It can happen at multiple OSI layers; although technically true
multiplexing only happens at layer 1 because its to do with the bits.

    (Layers 2 and 3 can do a form of multiplexing though!)


### Different types of multiplexing:
Time division multiplexing
Frequency division multiplexing
Space division multiplexing
    *I dont think you need these for exam.*


### Fake multiplexing:
"Fake multiplexing" is when higher up OSI layers break data up by themselves.
This shouldn't really be called multiplexing, but it does the same thing.

### Fake Multiplexing EXAMPLE:

Bob sends 2 gigabytes of data to Alice; UDP on ipv4 with ethernet frame.

The computer / routers at level 2 are like: HELL NO! Multiplex that shit!
The routers break the data up into 1 megabyte parts.

the 1 megabyte bits are sent through the network:
The ISP (internet service provider) is like: HELL NO! 1 megabyte each???
That's too big, Multiplex that shit!

the ISP breaks up the data into 2 kilobytes each. 

<transmission_continues.....>

The UDP packets reach their destination.

ISP de-multiplexes the data into their original 1 megabyte forms

Router/computer de-multiplexes the data into it's original 1 gigabyte form.


