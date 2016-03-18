#creation of dictionary with key=sequence ID and values = tuples of (sequence, structure)
#Created 26/02/16 by Quentin Thomas

lst = open('../input/dssp.3line','r').read().splitlines()
dict={}
for line in range(0,int(len(lst)),3):
	dict[lst[line]] = (lst[line+1], lst[line+2])
print dict