# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 16:04:24 2016

@author: thomas
"""

f = open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/topology.txt','r').read().splitlines()
f2 = open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/fasta_files/topology_files/sequence.fasta','w')
count=1
file_count = 0
for lines in f:
    count=count+1
    if count == 2:
        file_count = file_count + 1
        f2=open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/fasta_files/topology_files/sequence' + str(file_count) + '.fasta','w')
        f2.write(lines + '\n')
        count = 0
    else:
        f2.write(lines + '\n')


f2.close()
