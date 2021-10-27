

"""
Sender side simulation of RDT 3.0;

Input packets are formatted
[type, seq_num, message]
0 message with seq_num to be send;
1 ACK received; acking seq_num;
2 timeout event; resend last packet; 

Output packets are formatted
[status, seq_num]
-1 unexpected packet, -1 as seq_num;
0 message sent successfully, seq_num is the seq # of the message;
1 ACK processed; seq_num is the ACk seq_num;
2 resending finished; seq_num is the seq_num of the resent message;

Four states as described in the FSM
0 - wait for data 0;
1 - wait for ack 0;
2 - wait for data 1;
3 - wait for ack 1;

"""

DATA_EV = 0
ACK_EV = 1
TIMEOUT_EV = 2

ERR = [-1,-1]

def RDT_sender(event,state):   
    '''
    event :: [ type, seq_num, data ]

    state :: integer (state number on diagram)

    RETURNS:
        (state, [status, seq_num])
    
    state: next state in FSM, seq
    '''
    if len(event) == 0:
        return (state, ERR)

    type = event[0]
    seq_num = None
    data = None
    if len(event) > 1:
        seq_num = event[1]
        if len(event) > 2:
            data = event[2]

    expected = state // 2 # data expected

    if (state % 2) == 0: # Waiting for data.
        if type == DATA_EV: # data event.
            if expected == seq_num:
                return (state + 1, [0, expected])
            else:
                return (state, ERR)
        else:
            return (state, ERR)
    else: # Waiting on ACK or TIMEOUT.
        if type == ACK_EV:
            if expected == seq_num:
                return ((state + 1) % 4, [1, expected])
            else:
                return (state, ERR)
        elif type == TIMEOUT_EV:
            return (state, [2, expected])
        else:
            return (state, [-1,-1])





#Do not modify the following lines    
def sndr_test(event_list):    
    state = 0
    action_list = []    
    
    for event in event_list:        
        state, action = RDT_sender(event,state)
        action_list.append(action)

    print(f'{action_list}')
    




def sndr_check(event_list):    
    state = 0
    action_list = []    
    
    for event in event_list:        
        state, action = RDT_sender(event,state)
        action_list.append(action)

    return action_list  



def check(ev, got):
    assert f"{sndr_check(ev)}" == f"{got}"
    print("SUCCESS")

sndr_test([[0, 0, 1], [1, 0, 1], [0, 1, 3], [2],[1,1,3]])

# EXPECTED: [[0, 0], [1, 0], [0, 1], [2, 1], [1, 1]]
# GOT:     [[0, 0], [1, 0], [0, 1], [-1, -1], [1, 1]]

