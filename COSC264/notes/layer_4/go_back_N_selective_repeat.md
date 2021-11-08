

# Go back N
### AND
# Selective repeat


we have a window size N.
    (able to send N frames)

In this example, Window size = 3,
                    (N = 3)

Thus the maximum number of frames we are allowed
to send without an ACK is 3.

__SEE_EXAMPLE_BELOW__.



# Selective repeat
Selective repeat is the same as Go back N,
except it ONLY SENDS BACK PACKETS that weren't ACKd.

This means that some packets must be stored in a buffer until
    the previous packets are re-sent.

_What is the upper layer?_
    The upper layer simply refers to the application that is using the sockets.
    Packets must be sent to the upper layer in order; which is why we will
    need a buffer to store frames sometimes. 
        (eg if A->B->C->D are sent, and B fails, C and D will have to be put in buffer,
                                        and sent to upper layer after B is resent.)




### Go back N and Selective repeat.
#### EXAMPLE:
```py
-----> Send 1 frame  (seq_num = 0)
-----> Send 1 frame  (seq_num = 1)
-----> Send 1 frame  (seq_num = 2)
        # In this case, 3 frames have been sent. 
        # Since three frames have been sent without a reply,
        # None more can be sent;
        # The sender must wait for ACKs.

<---- ACK 2  # Acknowledge frame 2 AND all frames before 2.

-----> Send 1 frame  (seq_num = 3)
-----> Send 1 frame  (seq_num = 4) # SAY, THIS PACKET IS LOST.
-----> Send 1 frame  (seq_num = 5)

<---- ACK 3
# Timeout for frame 4!!!
    # Time waiting is arbitrary, similar to stop_&_wait.
<---- ACK 5 (This ACK exists under selective repeat ONLY.) 

# Since frame 4 and 5 weren't acknowledged, frame 4 AND 5
# must be sent back (under Go back N).
# Under selective repeat, only frame 4 needs to be resent.

-----> Send 1 frame  (seq_num = 4)
-----> Send 1 frame  (seq_num = 5) 
# NOTE:: Selective repeat wouldn't send back frame 5, 
    # and would rather store the old one in a buffer!

<---- ACK 5  # If Go-Back-N- assumes 4 and 5 have been recvd.
    'OR'
<---- ACK 4  # If selective repeat.



```




