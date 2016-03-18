#Created 24/02/2016 by Quentin Thomas
#Extraction features from sequences and structure
w = open("../output/extracted_features", "w")
x = open("../input/testfile.txt", "r")
lst=x.read().splitlines()   #readthefile and split each line
name = lst[0]               #record the name of the sequence in "name"
seq = list(lst[1])          #record the sequence of nucleotide in "seq"
stru = list(lst[2])         #record the structure in "stru"
lst3 = {'A':1,'R':2,'N':3,'D':4,'C':5,'Q':6,'E':7,'G':8,'H':9,'I':10,'L':11,'K':12,'M':13,'F':14,'P':15,'S':16,'T':17,'W':18,'Y':19,'V':20}
                            #lst3 is a dictionary of amino acid and a given value
a=[]                        #a is an empty string to store aminoacid values
b=[]                        #b is an empty string to store structure scores
c=[]			    #c is an empty string to store data from a and b
for amino in seq:           #loop over the sequence
	if amino in lst3:
		a.append(str(lst3[amino]))
for feature in stru:
	if feature == 'H':
		b.append('1')
	else:
		b.append('-1')
c = [v + ' ' + a[i] + ':1'  for i, v in enumerate(b)]
w.write(name)
for string in c:
	w.write(string + '\n')
w.close()




