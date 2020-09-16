import numpy as np
def pooling(Mj, theta, transmit_util, receive_util):
    PBE = []
    if Mj == 1:
        p = theta
        Util_receiver_for_A1 = p * receive_util[1][Mj][1] + (1-p) * receive_util[2][Mj][1]
        Util_receiver_for_A2 = p * receive_util[1][Mj][2] + (1-p) * receive_util[2][Mj][2]
        
        Aj = 1 if Util_receiver_for_A1 > Util_receiver_for_A2 else 2
        
        if transmit_util[1][1][Aj] >= transmit_util[1][2][1] and transmit_util[2][1][Aj] >= transmit_util[2][2][1]:
            temp = (receive_util[1][2][1] + receive_util[2][2][2] - receive_util[2][2][1] - receive_util[1][2][2])
            q = (receive_util[2][2][2] - receive_util[2][2][1]) / temp
            F1_empty = 0
            q_min = -1
            q_max = -1
            if temp > 0 and q > 1:
                F1_empty = 1
            elif temp > 0 and q <= 1:
                q_min = max(q, 0)
                q_max = 1 
            elif temp < 0 and q < 0:
                F1_empty = 1
            elif temp < 0 and q >= 0:
                q_min = 0
                q_max = min(q, 1)
            elif temp == 0 and receive_util[2][2][1] >= receive_util[2][2][2]:
                q_min = 0
                q_max = 1
            elif temp == 0 and receive_util[2][2][1] < receive_util[2][2][2]:
                F1_empty = 1
            
            if not F1_empty:
                EU_R = theta * receive_util[1][1][Aj]  + (1 - theta) * receive_util[2][1][Aj]
                EU_S = theta * transmit_util[1][1][Aj] + (1 - theta) * transmit_util[2][1][Aj]
                S1 = ('M{}, M{}'.format(Mj, Mj))
                S2 = ('A{}, A{}'.format(Aj, 1))
                PBE.append({'type':1, 'S1':S1, 'S2':S2, 'q_range':(q_min, q_max), 'p_range':(p, p), 'EU_S':EU_S, 'EU_R':EU_R})
    
        if transmit_util[1][1][Aj] >= transmit_util[1][2][2] and transmit_util[2][1][Aj] >= transmit_util[2][2][2]:
            temp = (receive_util[1][2][1] + receive_util[2][2][2] - receive_util[2][2][1] - receive_util[1][2][2])
            q = (receive_util[2][2][2] - receive_util[2][2][1]) / temp
            F2_empty = 0
            q_min = -1
            q_max = -1
            if temp > 0 and q < 0:
                F2_empty = 1
            elif temp > 0 and q >= 0:
                q_min = 0
                q_max = min(q ,1)
            elif temp < 0 and q > 1:
                F2_empty = 1
            elif temp < 0 and q <= 1:
                q_min = max(q, 0)
                q_max = 1
            elif temp == 0 and receive_util[2][2][1] <= receive_util[2][2][2]:
                q_min = 0
                q_max = 1
            elif temp == 0 and receive_util[2][2][1] > receive_util[2][2][2]:
                F2_empty = 1
            
            if not F2_empty:
                EU_R = theta * receive_util[1][1][Aj]  + (1 - theta) * receive_util[2][1][Aj]
                EU_S = theta * transmit_util[1][1][Aj] + (1 - theta) * transmit_util[2][1][Aj]
                S1 = ('M{}, M{}'.format(Mj, Mj))
                S2 = ('A{}, A{}'.format(Aj, 2))
                PBE.append({'type':1, 'S1':S1, 'S2':S2, 'q_range':(q_min, q_max), 'p_range':(p, p), 'EU_S':EU_S, 'EU_R':EU_R})
        return PBE
    elif Mj == 2:
        q = theta   
        Util_receiver_for_A1 = q * receive_util[1][Mj][1] + (1-q) * receive_util[2][Mj][1]
        Util_receiver_for_A2 = q * receive_util[1][Mj][2] + (1-q) * receive_util[2][Mj][2]
        
        Aj = 1 if Util_receiver_for_A1 > Util_receiver_for_A2 else 2
        
        if transmit_util[1][2][Aj] >= transmit_util[1][1][1] and transmit_util[2][2][Aj] >= transmit_util[2][1][1]:
            temp = (receive_util[1][1][1] + receive_util[2][1][2] - receive_util[2][1][1] - receive_util[1][1][2])
            p = (receive_util[2][1][2] - receive_util[2][1][1]) / temp
            F1_empty = 0
            p_min = -1
            p_max = -1
            if temp > 0 and p > 1:
                F1_empty = 1
            elif temp > 0 and p <= 1:
                p_min = max(p, 0)
                p_max = 1 
            elif temp < 0 and p < 0:
                F1_empty = 1
            elif temp < 0 and p >= 0:
                p_min = 0
                p_max = min(p, 1)
            elif temp == 0 and receive_util[2][1][1] >= receive_util[2][1][2]:
                p_min = 0
                p_max = 1
            elif temp == 0 and receive_util[2][1][1] < receive_util[2][1][2]:
                F1_empty = 1
            
            if not F1_empty:
                EU_R = theta * receive_util[1][2][Aj]  + (1 - theta) * receive_util[2][2][Aj]
                EU_S = theta * transmit_util[1][2][Aj] + (1 - theta) * transmit_util[2][2][Aj]
                S1 = ('M{}, M{}'.format(Mj, Mj))
                S2 = ('A{}, A{}'.format(1, Aj))
                PBE.append({'type':2, 'S1':S1, 'S2':S2, 'q_range':(q, q), 'p_range':(p_min, p_max), 'EU_S':EU_S, 'EU_R':EU_R})

        if transmit_util[1][2][Aj] >= transmit_util[1][1][2] and transmit_util[2][2][Aj] >= transmit_util[2][1][2]:
            temp = (receive_util[1][1][1] + receive_util[2][1][2] - receive_util[2][1][1] - receive_util[1][1][2])
            p = (receive_util[2][1][2] - receive_util[2][1][1]) / temp
            F2_empty = 0
            p_min = -1
            p_max = -1
            if temp > 0 and p < 0:
                F2_empty = 1
            elif temp > 0 and p >= 0:
                p_min = 0
                p_max = min(p ,1)
            elif temp < 0 and p > 1:
                F2_empty = 1
            elif temp < 0 and p <= 1:
                p_min = max(p, 0)
                p_max = 1
            elif temp == 0 and receive_util[2][1][1] <= receive_util[2][1][2]:
                p_min = 0
                p_max = 1
            elif temp == 0 and receive_util[2][1][1] > receive_util[2][1][2]:
                F2_empty = 1
            
            if not F2_empty:
                EU_R = theta * receive_util[1][2][Aj]  + (1 - theta) * receive_util[2][2][Aj]
                EU_S = theta * transmit_util[1][2][Aj] + (1 - theta) * transmit_util[2][2][Aj]
                S1 = ('M{}, M{}'.format(Mj, Mj))
                S2 = ('A{}, A{}'.format(2, Aj))
                PBE.append({'type':2, 'S1':S1, 'S2':S2, 'q_range':(q, q), 'p_range':(p_min, p_max), 'EU_S':EU_S, 'EU_R':EU_R})
        return PBE