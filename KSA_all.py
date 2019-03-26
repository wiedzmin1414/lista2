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

def KSA_STT(N,Key):
    Key = binary_word(Key)
    S = [i for i in range(0,N)]
    licznik = 0
    j = 0
    count_of_marked_items = 0
    count_of_items = len(S)
    marked_item_list = [False]*count_of_items
    threshhold = (count_of_items-1)/2
    while(count_of_marked_items != count_of_items):
        i = licznik % N
        j =(j + S[i % N] + Key[licznik % len(Key)]) % N
        S[i % N] , S[j % N] = S[j % N] , S[i % N]
        
        if count_of_marked_items < threshhold:
            if marked_item_list[i] == False and marked_item_list[j] == False:
                marked_item_list[i] == True
                count_of_marked_items += 1
        else:
            if (marked_item_list[i] == False and marked_item_list[j] == True) or (i == j):
                marked_item_list[i] == True
                count_of_marked_items += 1
        licznik += 1
        marked_item_list[i], marked_item_list[j] = marked_item_list[j], marked_item_list[i] #swap
    return S

def KSA_RS(N,T,Key):
    S = [i for i in range(0,N)]
    L = len(Key)
    #Key = binary_word(Key)
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