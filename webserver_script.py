import pandas as pd
from math import exp
import subprocess

#.................run psi-blast.......................................


subprocess.call('blastpgp -a 3 -j 3 -d /home/thomas/blast/uniref90.fasta -i '!!!!INSERT INPUT_SEQUENCE!!!!!' -o /home/thomas/Desktop/19-02-2016-DSSPhelix-project/webserver/psi_file.psi', shell=True)


#..................process psi-output..................................

subprocess.call("tail -n +4 /home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/psi_file.psi | head -n -6 | awk '{ print  $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14, $15, $16, $17, $18, $19, $20, $21, $22 }'  >/home/thomas/Desktop/19-02-2016-DSSPhelix-project/webserver/matrice.psi", shell=True)

#.................process psi-matrice................................

matrice = open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/webserver/matrice.psi','r')
feature_svm=open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/webserver/feature.svm','w')
y=open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/webserver/feature1.svm','w')
DataFrame=pd.read_csv(matrice,engine='python', sep=' ', header=0, names=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'])
proba = lambda x : float(1/(1+exp(-x)))
ProbaFrame = DataFrame.applymap(proba)
b = map(list, ProbaFrame.values)
x=[]
for line in b:
    x.append(str(0))
    for i, c in enumerate(line): 
        y.write(str(i+1) + ':' + str(c) + ' ')
    y.write('\n')
y.close()
b=open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/webserver/feature1.svm','r').read().splitlines()
result=zip(x,b)
for a,b in result:
    feature_svm.write(str(a)+ ' ' +str(b)+'\n')

    
#...................run svm_classify...............................
    
subprocess.call('/home/thomas/svm_light/svm_classify /home/thomas/Desktop/19-02-2016-DSSPhelix-project/webserver/feature.svm /home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/cross_validation_svm/svm_models_pred/psi_blast/Models_psi/final_model_kernel2.svm /home/thomas/Desktop/19-02-2016-DSSPhelix-project/webserver/prediction.pred', shell=True)

#................prediction output..................................


target_pred = open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/webserver/prediction.pred','r').read().splitlines()
u=[]
for lines in target_pred:
    if lines[0] != '-':
        u.append('H')
    else:
        u.append('-')
print ''.join(u)

