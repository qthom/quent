# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 15:54:34 2016

@author: thomas
"""
import sys
input_file1 = sys.argv[1]
input_file2 = sys.argv[2]
output_file = sys.argv[3]

i=open(output_file,'w')
psi_features = open(input_file1,'r').read().splitlines()        

target_features=[]        
topology=open(input_file2,'r').read().splitlines()
y=topology[0]
x=topology[1]
for amino in x:
    if amino == 'H':
        target_features.append('1')
    else:
        target_features.append('-1')
        
result=zip(target_features, psi_features)
for a,b in result:
    i.write(str(a)+ ' ' +str(b)+'\n')
 