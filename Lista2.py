# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 22:15:23 2019

@author: mateu
"""

from PRGA_all import *
from KSA_all import *

def RC4(N,Key):
    S = KSA(N,N,Key)
    return PRGA(S,N)

def RC4_drop(N,Key,Drop):
    S = KSA(N,N,Key)
    return PRGAdrop(S,N,Drop)

def RC4_RS(N,T,Key,): #l - length 
    S = KSA_RS(N,T,Key)
    return PRGA(S,N)

def RCT_SST(N,Key,Drop):
    S = KSA_STT(N,Key)
    return PRGAdrop(S,N,Drop)

for i in RC4_drop(256,'Wiki',127):  
    print(i)
