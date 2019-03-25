# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 18:27:05 2019

@author: mateu
"""

from slowa import *

def KSA(N,T,Key):
    Key = bytes_word(Key)
    S = [i for i in range(0,N)]
    j = 0
    for i in range(0,T):
        j =(j + S[i % N] + Key[i % len(Key)]) % N
        S[i % N] , S[j % N] = S[j % N] , S[i % N]
        #print(i, j)
        #print(S)
    return S

def KSA_RS(N,T,Key):
    S = [i for i in range(0,N)]
    L = len(Key)
    for r in range(0,T):
        print(S)
        Top = []
        Bot = []
        for i in range(0,N+1):
            if Key[(r*N + i) % L ] == 0:
                Top.append(i)
            else:
                Bot.append(i)
        print(Top, '###',Bot)
        S = Top + Bot
        print(S)
    return S