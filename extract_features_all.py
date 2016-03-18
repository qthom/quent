#Created 25/02/2016 by Quentin Thomas
#Extraction features from sequences and structure
#Modified last 26/02/2016

'''w = open("../output/extracted _features_sets/extracted_features_set1", "w")
lst = open("../output/cross_validation_sets/cross_validation_sets1.txt" , "r").read().splitlines()
dicti = {'A':1,'R':2,'N':3,'D':4,'C':5,'Q':6,'E':7,'G':8,'H':9,'I':10,'L':11,'K':12,'M':13,'F':14,'P':15,'S':16,'T':17,'W':18,'Y':19,'V':20}
header = ('# A:1 R:2 N:3 D:4 C:5 Q:6 E:7 G:8 H:9 I:10 L:11 K:12 M:13 F:14 P:15 S:16 T:17 W:18 Y:19 V:20')
w.write(header + '\n')
a=[]
b=[]
c=[]
seq=[]
name=[]
stru=[]
while lst:
	stru = list(lst.pop())
	seq = list(lst.pop())
	name = lst.pop()
	for amino, feature in zip(seq,stru):
		if amino in dicti:
			a.append(str(dicti[amino]))
		else:
			a.append('0')
		if feature == 'H':
			b.append('1')
		else:
			b.append('-1')
c = [v + ' ' + a[i] + ':1'  for i, v in enumerate(b)]
for string in c:
	w.write(string + '\n')'''


#w = open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/cross_validation_svm/extracted_features_sets/basic/concatenate_features/features_2345.txt', "w")
#lst = open("/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/cross_validation_svm/extracted_features_sets/basic/test_concatenate_sets/test_sets_2345.txt" , "r").read().splitlines()
dicti = {'A':1,'R':2,'N':3,'D':4,'C':5,'Q':6,'E':7,'G':8,'H':9,'I':10,'L':11,'K':12,'M':13,'F':14,'P':15,'S':16,'T':17,'W':18,'Y':19,'V':20}

a=[]
b=[]
c=[]
seq=[]
stru=[]
dic={}

mkeys=[]

for lines in range(0,int(len(lst)),3):
    dic[lst[lines]] = (lst[lines+1], lst[lines+2])
    mkeys.append(lst[lines])
 
for key in mkeys:
    seq = dic[key][0]
    stru = dic[key][1]
    
    for amino, feature in zip(seq,stru):
        if amino in dicti:
            a.append(str(dicti[amino]))
        else:
            a.append('0')
        if feature == 'H':
            b.append('1')
        else:
            b.append('-1')
c = [v + ' ' + a[i] + ':1'  for i, v in enumerate(b)]
for string in c:
	w.write(string + '\n')

w.close()