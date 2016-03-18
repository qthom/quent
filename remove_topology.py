#Created 26/02/2016 by Quentin Thomas
#Extraction features from sequences and structure
#Modified last 26/02/2016

w = open("../output/sequence2.txt", "w")
lst = open("../input/dssp.3line" , "r").read().splitlines()
seq=[]
name=[]
stru=[] 	
while lst:	
	stru = lst.pop()
	seq = lst.pop()
	name = lst.pop()
	w.write(name + '\n' + seq + '\n')