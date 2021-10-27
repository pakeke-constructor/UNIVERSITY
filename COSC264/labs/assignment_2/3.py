"""
Sender side simulation of GBN;

An event is formatted as
[type, seq_num, data]
0 data to send; no check on seq_num and data;
1 ACK received; acking seq_num;
2 timeout event; resend all outgoing unAck'ed events; no check on seq_num and data;

Output of function GBN_sender() is formatted as
[status, base, next_seq]
-1 unexpected event/window full
0 data sent successfully
1 ACK processed; 
2 resending finished; 

N - the window size
base - seq# of lower winder boundary (base)

"""

N = 4 #window size;

def isfull(base, next_seq):
    return (next_seq - base) < N



def GBN_sender(event,base,next_seq):
    '''
    

    returns:  [status, base, next_seq]
    '''
    seq_num = None
    data = None
    if len(event) > 1:
        seq_num = event[1]
        if len(event) > 2:
            data = event[2]

    if event[0] == 0: # Data to send; check whether the window is full;
        if isfull(base, next_seq):
            return [0, base, next_seq + 1]
        else:
            return [-1, base, next_seq]

    if event[0] == 1: # ACK to process;
        if (base is None or next_seq is None):
            return [-1, base, next_seq]
        if not (base <= seq_num <= (next_seq - 1)):
            return [-1, base, next_seq]
        base = seq_num + 1
        return [1, base, max(base, next_seq)]

    if event[0] == 2:# timeout event
        return [2, base, next_seq]
                

#Do NOT modify the following code    
def sndr_test(event_list):    
    base = 0
    next_seq = 0
    action_list = []    
    
    for event in event_list:        
        action = GBN_sender(event,base,next_seq)
        base = action[1]
        next_seq = action[2]
        action_list.append(action)    
        
    print(f'{action_list}')
