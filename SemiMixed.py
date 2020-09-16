import numpy as np
def semimixed(theta, transmit_util, receive_util):
    PBE = []
    Kr = ((receive_util[1][1][1] - receive_util[1][1][2]) * (receive_util[2][2][1] - receive_util[2][2][2]) - \
          (receive_util[1][2][1] - receive_util[1][2][2]) * (receive_util[2][1][1] - receive_util[2][1][2])) * theta * (1 - theta)
    if Kr == 0:
        pass
    else:
        m1 = (1 / Kr) * (1 - theta) * (receive_util[2][1][2] - receive_util[2][1][1]) * \
             ((theta * (receive_util[1][2][1] - receive_util[1][2][2])) - \
              ((1 - theta) * (receive_util[2][2][1] - receive_util[2][2][2])))

        m2 = (1 / Kr) * theta * (receive_util[1][1][1] - receive_util[1][1][2]) * \
             ((theta * (receive_util[1][2][1] - receive_util[1][2][2])) - \
              ((1 - theta) * (receive_util[2][2][1] - receive_util[2][2][2])))
        m_star = max(m1, m2, 1 - m1, 1 - m2)
        if m_star == 1 - m2:
            if receive_util[1][1][1] >= receive_util[1][1][2] and \
                    transmit_util[2][1][1] <= min(transmit_util[2][2][1], transmit_util[2][2][2]):
                m1_hat = (m1 - m2) / (1 - m2)
                m2_hat = 0
                a1_hat = 1
                a2_hat = (transmit_util[1][1][1] - transmit_util[1][2][2]) / (transmit_util[1][2][1] - transmit_util[1][2][2])
            elif receive_util[1][1][1] <= receive_util[1][1][2] and \
                    transmit_util[2][1][2] <= min(transmit_util[2][2][1], transmit_util[2][2][2]):
                m1_hat = (m1 - m2) / (1 - m2)
                m2_hat = 0
                a1_hat = 0
                a2_hat = (transmit_util[1][1][2] - transmit_util[1][2][2]) / (transmit_util[1][2][1] - transmit_util[1][2][2])
            else:
                return PBE
        elif m_star == m2:
            if receive_util[1][2][1] >= receive_util[1][2][2] and \
                    transmit_util[2][2][1] <= min(transmit_util[2][1][1], transmit_util[2][1][2]):
                m1_hat = m1 / m2
                m2_hat = 1
                a1_hat = (transmit_util[1][2][1] - transmit_util[1][1][2]) / (transmit_util[1][1][1] - transmit_util[1][1][2])
                a2_hat = 1
            elif receive_util[1][2][1] <= receive_util[1][2][2] and \
                    transmit_util[2][2][2] <= min(transmit_util[2][1][1], transmit_util[2][1][2]):
                m1_hat = m1 / m2
                m2_hat = 1
                a1_hat = (transmit_util[1][2][2] - transmit_util[1][1][2]) / (transmit_util[1][1][1] - transmit_util[1][1][2])
                a2_hat = 0
            else:
                return PBE
        elif m_star == 1 - m1:
            if receive_util[2][1][1] >= receive_util[2][1][2] and \
                    transmit_util[1][1][1] <= min(transmit_util[1][2][1], transmit_util[1][2][2]):
                m1_hat = 0
                m2_hat = (m2 - m1) / (1 - m1)
                a1_hat = 1
                a2_hat = (transmit_util[2][1][1] - transmit_util[2][2][2]) / (transmit_util[2][2][1] - transmit_util[2][2][2])
            elif receive_util[2][1][1] <= receive_util[2][1][2] and \
                    transmit_util[1][1][2] <= min(transmit_util[1][2][1], transmit_util[1][2][2]):
                m1_hat = 0
                m2_hat = (m2 - m1) / (1 - m1)
                a1_hat = 0
                a2_hat = (transmit_util[2][1][2] - transmit_util[2][2][2]) / (transmit_util[2][2][1] - transmit_util[2][2][2])
            else:
                return PBE
        elif m_star == m1:
            if receive_util[2][2][1] >= receive_util[2][2][2] and \
                    transmit_util[1][2][1] <= min(transmit_util[1][1][1], transmit_util[1][1][2]):
                m1_hat = 1
                m2_hat = m2 / m1
                a1_hat = (transmit_util[2][2][1] - transmit_util[2][1][2]) / (transmit_util[2][1][1] - transmit_util[2][1][2])
                a2_hat = 1
            elif receive_util[2][2][1] <= receive_util[2][2][2] and \
                    transmit_util[1][2][2] <= min(transmit_util[1][1][1], transmit_util[1][1][2]):
                m1_hat = 1
                m2_hat = m2 / m1  
                a1_hat = (transmit_util[2][2][2] - transmit_util[2][1][2]) / (transmit_util[2][1][1] - transmit_util[2][1][2])
                a2_hat = 0
            else:
                return PBE
        if a1_hat >= 0 and a1_hat <= 1 and a2_hat >= 0 and a2_hat <= 1:
            EU_S_t1 = m1_hat * (a1_hat * transmit_util[1][1][1] + (1 - a1_hat) * transmit_util[1][1][2]) + \
                      (1 - m1_hat) * (a2_hat * transmit_util[1][2][1] + (1 - a2_hat) * transmit_util[1][2][2])
            EU_S_t2 = m2_hat * (a1_hat * transmit_util[2][1][1] + (1 - a1_hat) * transmit_util[2][1][2]) + \
                      (1 - m2_hat) * (a2_hat * transmit_util[2][2][1] + (1 - a2_hat) * transmit_util[2][2][2])
            EU_S = (theta * EU_S_t1) + ((1 - theta) * EU_S_t2)
            
            EU_R_M1 = ((a1_hat * ((m1_hat * receive_util[1][1][1] * theta) + (m2_hat * receive_util[2][1][1] * (1 - theta)))) + \
                      ((1 - a1_hat) * ((m1_hat * receive_util[1][1][2] * theta) + (m2_hat * receive_util[2][1][2] * (1 - theta))))) / \
                      ((m1_hat * theta) + (m2_hat * (1 - theta)))

            EU_R_M2 = ((a2_hat * (((1 - m1_hat) * receive_util[1][2][1] * theta) + ((1 - m2_hat) * receive_util[2][2][1] * (1 - theta)))) + \
                      ((1 - a2_hat) * (((1 - m1_hat) * receive_util[1][2][2] * theta) + ((1 - m2_hat) * receive_util[2][2][2] * (1 - theta))))) / \
                      (((1 - m1_hat) * theta) + ((1 - m2_hat) * (1 - theta)))
            q_M1 = (m1_hat * theta) + (m2_hat * (1 - theta))
            q_M2 = 1 - q_M1
            EU_R = (q_M1 * EU_R_M1) + (q_M2 * EU_R_M2)
            S1 = ('M1:{}, M2:{}'.format(m1_hat, m2_hat))
            S2 = ('A1:{}, A2:{}'.format(a1_hat, a2_hat))
            
            PBE.append({'type':5, 'S1':S1, 'S2':S2, 'EU_S':EU_S, 'EU_R':EU_R})
    return PBE
