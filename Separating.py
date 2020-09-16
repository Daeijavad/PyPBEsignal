import numpy as np
def separating(theta, transmit_util, receive_util):
    PBE = []
    # (M1, M2)
    S1 = ('M{}, M{}'.format(1, 2))
    p = 1
    q = 0

    Ai = 1 if receive_util[1][1][1] > receive_util[1][1][2] else 2
    Aj = 1 if receive_util[2][2][1] > receive_util[2][2][2] else 2

    if transmit_util[1][1][Ai] >= transmit_util[1][2][Aj] and transmit_util[2][2][Aj] >= transmit_util[2][1][Ai]:
        EU_R = theta * receive_util[1][1][Ai] + (1 - theta) * receive_util[2][2][Aj]
        EU_S = theta * transmit_util[1][1][Ai] + (1 - theta) * transmit_util[2][2][Aj]
        S2 = ('A{}, A{}'.format(Ai, Aj))
        PBE.append({'type':3, 'S1':S1, 'S2':S2, 'q_range':(q, q), 'p_range':(p, p), 'EU_S':EU_S, 'EU_R':EU_R})
    # (M2, M1)
    S1 = ('M{}, M{}'.format(2, 1))
    p = 0
    q = 1

    Ai = 1 if receive_util[2][1][1] > receive_util[2][1][2] else 2
    Aj = 1 if receive_util[1][2][1] > receive_util[1][2][2] else 2

    if transmit_util[1][1][Ai] <= transmit_util[1][2][Aj] and transmit_util[2][2][Aj] <= transmit_util[2][1][Ai]:
        EU_R = theta * receive_util[1][2][Ai] + (1 - theta) * receive_util[2][1][Aj]
        EU_S = theta * transmit_util[1][2][Ai] + (1 - theta) * transmit_util[2][1][Aj]
        S2 = ('A{}, A{}'.format(Ai, Aj))
        PBE.append({'type':3, 'S1':S1, 'S2':S2, 'q_range':(q, q), 'p_range':(p, p), 'EU_S':EU_S, 'EU_R':EU_R})

    return PBE