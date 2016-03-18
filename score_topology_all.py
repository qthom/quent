#Created 04/03/2016 by Quentin Thomas
#Extraction features from sequences and structure
#Modified last 04/03/2016

w = open("../output/score_topology_all.txt", "w")
lst = open("../input/dssp.3line" , "r").read().splitlines()

dic={}
for lines in range(0,int(len(lst)),3):
    dic[lst[lines]] = (lst[lines+2])


    
    
