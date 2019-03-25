# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 18:56:54 2019

@author: mateu
"""

def PRGA(S,N): #l - length 
    i = 0
    j = 0
    w = []
    while True:
        i = (i+1) % N
        j = (j + S[i]) % N
        S[i] , S[j] = S[j], S[i]
        Z = S[ (S[i]+S[j]) % N ]
        print(Z)
    return w

def PRGAdrop(S,N,D): #l - length 
    i = 0
    j = 0
    w = []
    d = 0
    while True:
        i = (i+1) % N
        j = (j + S[i]) % N
        S[i] , S[j] = S[j], S[i]
        if d < D:
            d += 1
        else:
            Z = S[ (S[i]+S[j]) % N ]
            print(Z)
    return w