# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 08:55:37 2016

@author: thomas
"""







lst = open('../input/dssp.3line','r').read().splitlines()
dict={}
c=[]
seq=[]
name=[]
stru=[]

while lst:
    stru = lst.pop()
    seq = lst.pop()
    name = lst.pop()
    '''for feature in stru:
    		if feature == 'H':
    			c.append('1')
    		else:
    			c.append('-1')'''
   