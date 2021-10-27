

"""
This is a program simulating the receiver side of GBN,
******************
Input packets are formatted as
[seq_num, data]

Output packets are formatted as
[status, exp_num]
0 - an ACK is sent;
-1 - unexpected packets received; 
*******************
"""



def GBN_Receiver(packet,exp_num):
    #Your code here
    if len(packet) < 2:
        return [-1, exp_num]
    
    seq_num, data = packet
    if seq_num == exp_num:
        return [0, exp_num + 1]
    return [-1, exp_num]


#Do NOT modify the following code    
def rcvr_test(packet_list):    
    action_list = []
    exp_num = 1
    
    for packet in packet_list:        
        action = GBN_Receiver(packet,exp_num)
        exp_num = action[1]
        action_list.append(action)    
        
    print(f'{action_list}')  

rcvr_test([[1,1]])
[[0, 2]]
rcvr_test([[1,1],[2,2]])
[[0, 2], [0, 3]]
rcvr_test([[1,1],[2,2],[3,3]])
[[0, 2], [0, 3], [0, 4]]
rcvr_test([[0,1]])