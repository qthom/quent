import re

lst = open('../input/dssp.3line','r').read().splitlines()
dict={}
for line in range(0,int(len(lst)),3):
    dict[lst[line]] = (lst[line+1], lst[line+2])

#...........................................................................................................................
   
'''f = open('../output/cross_validation_svm/cross_validation_ids.txt','w')
clus= open('../output/formated_cluster.txt', 'r').read().splitlines()
file_count=0
count=0
for lines in clus:
    iD= re.split('... |    |,', lines)
    iDs=iD[1]
    index=lines[0]
    count=count+1
    if index == '0' and count >= 65:
        file_count=file_count+1
        f= open('../output/cross_validation_sets/cross_validation_ids' + str(file_count) + '.txt','w')
        f.write(iDs +'\n')
        count=0
    else:
        f.write(iDs +'\n')
             
f.close()'''

#............................................................................................................................

ff=open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/cross_validation_svm/sets_id/Set_ids/cross_validation_ids2.txt','r').read().splitlines()
f=open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/cross_validation_svm/sets_id/Set_3line/cross_validation_sets2.txt','w')
seq=''
topo=''

for l in ff:
    seq = dict[l][0]
    topo = dict[l][1]
    f.write(l + '\n' + seq + '\n' + topo+ '\n' )


f.close()


#................................................................................................................................................

w = open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/cross_validation_svm/extracted_features_sets/basic/6_sets/extracted_feature_set2.txt', "w")
lst = open("/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/cross_validation_svm/sets_id/Set_3line/cross_validation_sets2.txt" , "r").read().splitlines()
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