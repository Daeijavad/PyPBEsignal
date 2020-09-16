import numpy as np
import Pooling
import Mixed
import SemiMixed
import Separating

def Eq(theta, transmit_util, receive_util):
    PBE = []
    PBE.extend(Pooling.pooling(Mj= 1, theta= theta,transmit_util= transmit_util, receive_util= receive_util))
    PBE.extend(Pooling.pooling(Mj= 2, theta= theta,transmit_util= transmit_util, receive_util= receive_util))
    PBE.extend(Separating.separating(theta= theta,transmit_util= transmit_util, receive_util= receive_util))
    PBE.extend(Mixed.mixed(theta= theta,transmit_util= transmit_util, receive_util= receive_util))
    PBE.extend(SemiMixed.semimixed(theta= theta,transmit_util= transmit_util, receive_util= receive_util))

    return PBE
