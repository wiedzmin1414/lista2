# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 22:15:23 2019

@author: mateu
"""

from PRGA_all import *
from KSA_all import *
from slowa import *



def RC4(N,Key):
    S = KSA(N,N,Key)
    return PRGA(S,N)

def RC4_drop(N,Key,Drop):
    S = KSA(N,N,Key)
    return PRGAdrop(S,N,Drop)

def RC4_RS(N,T,Key,length): #l - length 
    S = KSA_RS(N,T,Key)
    i = 0
    j = 0
    w = []
    for xDDx in range(0,length):
        i = (i+1) % N
        j = (j + S[i]) % N
        S[i] , S[j] = S[j], S[i]
        Z = S[ (S[i]+S[j]) % N ]
        w.append(Z)
    return w

    
def RC4_drop(N,T,Key,D):
    return RC4(N,T,Key)[D::]


