

# Control Registers:


_PC_:  Program counter
    Address of next instruction


_SP_:  Stack pointer
    points to top of stack

_STATUS_:  Status flag of last operation. (Like an enum!)
    Flags:
        C: Carry
        N: Negative
        V: Overflow
        Z: Zero
    Contains metadata about operations completed in the CPU.
    Not set by programs, but read by programs


## NOTE::::
The stack memory is always at the top of memory arch,
so it will never run into other memory when allocating new space.

