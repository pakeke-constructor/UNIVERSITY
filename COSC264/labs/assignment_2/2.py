

ERR=[-1,-1]

def RDT_Receiver(packet):
    #Your code here:

    if len(packet) < 1:
        return ERR

    seq_num, data = packet

    if seq_num not in [0,1]:
        return ERR
    else:
        return [0, seq_num]
       




#Do NOT modify the following lines    
def rcvr_test(packet_list):    
    action_list = []    
    
    for packet in packet_list:        
        action = RDT_Receiver(packet)
        action_list.append(action)    
        
    print(f'{action_list}')  

rcvr_test([[0, 1]])
