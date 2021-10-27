
# Simple:
Keep sending too and from messenges.
(1 frame per message. Think like a packet.)

If you don't recieve a reply, send it again
after a specified time period.

Example:


----->  Send
<-----  Recv
----->  Send
<-----  Recv
----->  Send
<-----  Recv
----->  Send
*No reply for X amount of time*
    :: assume packet is lost
----->  Send
<-----  Recv
----->  Send
 ETC.




