
# Medium Access Control (MAC)

MAC is the process used to send and recieve frames across the network.

It is also responsible for error checking incoming frames via FCS 
(frame check sequence,)
And is in charge of adding FCS checks to the end of sending frames.



# MAC address:

A MAC address is a unique address that every device has, assigned
by the hardware manufacturer.
(Yup, you heard me, EVERY DEVICE has a unique MAC address. No Iphone will
have the same MAC address, for example.)

MAC ADDRESSES (usually) NEVER CHANGE.

When packets are recieved, the router will find the device via it's MAC
address.
If two devices have the same MAC address on the same LAN, then frames
will be sent to either device seemingly "randomly."
This is very bad, and is usually the result of bad hardware manufacturers.

#### mac address size:
-  6 bytes -->  2^(6*8) numbers
- Therefore, roughly 200 trillion MAC addresses are available.

*Will they ever be exhausted?*
TL;DR: No.  Hardware manufacturers should be able to continue making devices
with unique MAC addresses for decades to come.




