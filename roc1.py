
import operator
import numpy as np
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
y1=[]
y11=[]
y2=[]
y22=[]
y3=[]
y33=[]
y4=[]
y44=[]
y5=[]
y55=[]


s1=open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/cross_validation_svm/svm_models_pred/psi_blast/prediction_psi/Kernel2/set1_psi_kernel2','r').read().splitlines()
yy1=open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/cross_validation_svm/extracted_features_sets/psi_blast/topo_sets/extracted_features_psi1.topo','r').read().splitlines()
s2=open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/cross_validation_svm/svm_models_pred/psi_blast/prediction_psi/Kernel2/set2_psi_kernel2','r').read().splitlines()
yy2=open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/cross_validation_svm/extracted_features_sets/psi_blast/topo_sets/extracted_features_psi2.topo','r').read().splitlines()
s3=open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/cross_validation_svm/svm_models_pred/psi_blast/prediction_psi/Kernel2/set3_psi_kernel2','r').read().splitlines()
yy3=open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/cross_validation_svm/extracted_features_sets/psi_blast/topo_sets/extracted_features_psi3.topo','r').read().splitlines()
s4=open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/cross_validation_svm/svm_models_pred/psi_blast/prediction_psi/Kernel2/set4_psi_kernel2','r').read().splitlines()
yy4=open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/cross_validation_svm/extracted_features_sets/psi_blast/topo_sets/extracted_features_psi4.topo','r').read().splitlines()
s5=open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/cross_validation_svm/svm_models_pred/psi_blast/prediction_psi/Kernel2/set5_psi_kernel2','r').read().splitlines()
yy5=open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/cross_validation_svm/extracted_features_sets/psi_blast/topo_sets/extracted_features_psi5.topo','r').read().splitlines()


#........................order input..........................................


tpl1=zip(yy1,s1)
tpl2=zip(yy2,s2)
tpl3=zip(yy3,s3)
tpl4=zip(yy4,s4)
tpl5=zip(yy5,s5)
tpl1.sort(key = operator.itemgetter(1),reverse = True)
tpl2.sort(key = operator.itemgetter(1),reverse = True)
tpl3.sort(key = operator.itemgetter(1),reverse = True)
tpl4.sort(key = operator.itemgetter(1),reverse = True)
tpl5.sort(key = operator.itemgetter(1),reverse = True)
for bla in tpl1:
    y1.append(int(bla[0]))
    y11.append(float(bla[1]))
for bla in tpl2:        
    y2.append(int(bla[0]))
    y22.append(float(bla[1]))
for bla in tpl3:       
    y3.append(int(bla[0]))
    y33.append(float(bla[1]))
for bla in tpl4:      
    y4.append(int(bla[0]))
    y44.append(float(bla[1]))
for bla in tpl5:       
    y5.append(int(bla[0]))
    y55.append(float(bla[1]))

#.........................roc_curves and roc_auc................................

fpr = dict()
tpr = dict()
roc_auc = dict()
for i in range():
    fpr[i], tpr[i], _ = roc_curve(y_true[:, i], y_score[:, i])
    roc_auc[i] = auc(fpr[i], tpr[i])


#...................ploting....................................................

for i in range(n_classes):
    plt.plot(fpr[i], tpr[i], label='ROC curve of class {0} (area = {1:0.2f})'
                                   ''.format(i, roc_auc[i]))

plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Some extension of Receiver operating characteristic to multi-class')
plt.legend(loc="lower right")
plt.show()'''




