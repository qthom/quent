# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 17:42:26 2016

@author: thomas
"""

w = open("../output/IDs.txt", "w")
lst = open("../input/dssp.3line" , "r").read().splitlines()
seq=[]
name=[]
stru=[] 	
while lst:	
	stru = lst.pop()
	seq = lst.pop()
	name = lst.pop()
	w.write(name + '\n')
 
w.close()

dic={}
w2=open("../output/IDs.txt", "r").read().splitlines()
count = 0
for ids in w2:
    count = count +1
    dic[ids] = ('sequence' +str(count)+'.cons')



o=open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/cross_validation_svm/sets_id/Set_ids/cross_validation_ids5.txt','r').read().splitlines()
t=open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/cross_validation_svm/extracted_features_sets/psi_blast/conservation_sets/extracted_features_psi5.cons','w')
for iDs in dic:
    if iDs in o:
        g=str(dic[iDs])
        v = open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/fasta_files/conservation/matrice/'+g).read()
        t.write(v)
        
t.close()