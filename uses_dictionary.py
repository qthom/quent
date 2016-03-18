lst = open('../input/dssp.3line','r').read().splitlines()
g=open('../output/formated_cluster.txt', 'r').read().splitlines()
dict={}
for lines in range(0,int(len(lst)),3):
	dict[lst[lines]] = (lst[lines+1], lst[lines+2])

