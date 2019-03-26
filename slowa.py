# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 18:28:27 2019

@author: mateu
"""
from functools import reduce

def binary(a,b):
    return format(a, 'b').zfill(b)

def binary_word(a):
    lista = [binary(ord(i),8) for i in a]
    lista2 = reduce( (lambda a,b: a+b), lista)
    return [int(i) for i in lista2]

def bytes_word(s):
    return [ord(i) for i in s]

