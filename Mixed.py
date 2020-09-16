import numpy as np
def mixed(theta, transmit_util, receive_util):
     PBE = []
     Ks = (transmit_util[1][2][1] - transmit_util[1][2][2]) * (transmit_util[2][1][1] - transmit_util[2][1][2]) - \
          (transmit_util[1][1][1] - transmit_util[1][1][2]) * (transmit_util[2][2][1] - transmit_util[2][2][2])
    
     Kr = ((receive_util[1][1][1] - receive_util[1][1][2]) * (receive_util[2][2][1] - receive_util[2][2][2]) - \
           (receive_util[1][2][1] - receive_util[1][2][2]) * (receive_util[2][1][1] - receive_util[2][1][2])) * theta * (1 - theta)
     if Ks == 0 or Kr == 0:
          pass
     else:
          m1 = (1 / Kr) * (1 - theta) * (receive_util[2][1][2] - receive_util[2][1][1]) * \
               ((theta * (receive_util[1][2][1] - receive_util[1][2][2])) - \
                ((1 - theta) * (receive_util[2][2][1] - receive_util[2][2][2])))

          m2 = (1 / Kr) * theta * (receive_util[1][1][1] - receive_util[1][1][2]) * \
               ((theta * (receive_util[1][2][1] - receive_util[1][2][2])) - \
                ((1 - theta) * (receive_util[2][2][1] - receive_util[2][2][2])))

          a1 = (1 / Ks) * \
               ((transmit_util[2][2][1] * (transmit_util[1][1][2] - transmit_util[1][2][2])) - \
                (transmit_util[2][1][2] * (transmit_util[1][2][1] - transmit_util[1][2][2])) - \
                (transmit_util[2][2][2] * (transmit_util[1][2][1] - transmit_util[1][1][2])))

          a2 = (1 / Ks) * \
               ((transmit_util[2][1][1] * (transmit_util[1][1][2] - transmit_util[1][2][2])) - \
                (transmit_util[2][1][2] * (transmit_util[1][1][1] - transmit_util[1][2][2])) - \
                (transmit_util[2][2][2] * (transmit_util[1][1][1] - transmit_util[1][1][2])))

          if min(m1, 1 - m1, m2, 1 - m2, a1, 1 - a1, a2, 1 - a2) >= 0:
               EU_S_t1 = (1 / Ks) * \
                    ((transmit_util[1][1][1] * transmit_util[1][2][2] * (transmit_util[2][1][2] - transmit_util[2][2][1])) + \
                     (transmit_util[1][2][1] * transmit_util[1][1][2] * (transmit_util[2][1][1] - transmit_util[2][2][2])) - \
                     (transmit_util[1][1][1] * transmit_util[1][2][1] * (transmit_util[2][1][2] - transmit_util[2][2][2])) - \
                     (transmit_util[1][1][2] * transmit_util[1][2][2] * (transmit_util[2][1][1] - transmit_util[2][2][1])))

               EU_S_t2 = ((-1) / Ks) * \
                    ((transmit_util[2][1][1] * transmit_util[2][2][2] * (transmit_util[1][1][2] - transmit_util[1][2][1])) + \
                     (transmit_util[2][2][1] * transmit_util[2][1][2] * (transmit_util[1][1][1] - transmit_util[1][2][2])) - \
                     (transmit_util[2][1][1] * transmit_util[2][2][1] * (transmit_util[1][1][2] - transmit_util[1][2][2])) - \
                     (transmit_util[2][1][2] * transmit_util[2][2][2] * (transmit_util[1][1][1] - transmit_util[1][2][1])))

               EU_S = (theta * EU_S_t1) + ((1 - theta) * EU_S_t2)

               EU_R_M1 = (receive_util[1][1][1] * receive_util[2][1][2]) - (receive_util[1][1][2] * receive_util[2][1][1]) / \
                         (receive_util[1][1][1] + receive_util[2][1][2] - receive_util[1][1][2] - receive_util[2][1][1])

               EU_R_M2 = (receive_util[1][2][1] * receive_util[2][2][2]) - (receive_util[1][2][2] * receive_util[2][2][1]) / \
                         (receive_util[1][2][1] + receive_util[2][2][2] - receive_util[1][2][2] - receive_util[2][2][1])
               q_M1 = (m1 * theta) + (m2 * (1 - theta))
               q_M2 = 1 - q_M1
               EU_R = (q_M1 * EU_R_M1) + (q_M2 * EU_R_M2)
            
               S1 = ('M1:{}, M2:{}'.format(m1, m2))
               S2 = ('A1:{}, A2:{}'.format(a1, a2))
            
               PBE.append({'type':4, 'S1':S1, 'S2':S2, 'EU_S':EU_S, 'EU_R':EU_R})
     return PBE