
import operator
import numpy as np
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt


s=open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/cross_validation_svm/svm_models_pred/psi_blast/prediction_psi/Kernel2/set5_psi_kernel2','r').read().splitlines()
yy=open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/cross_validation_svm/extracted_features_sets/psi_blast/topo_sets/extracted_features_psi5.topo','r').read().splitlines()
s1=open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/final_model_optimized.pred','r').read().splitlines()
yy1=open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/cross_validation_svm/extracted_features_sets/psi_blast/topo_sets/extracted_features_psi.topo','r').read().splitlines()
s2=open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/final_model_kernel2.pred','r').read().splitlines()
yy2=open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/cross_validation_svm/extracted_features_sets/psi_blast/topo_sets/extracted_features_psi.topo','r').read().splitlines()
s3=open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/results/final_pred_conservation_default_Kernel.cons','r').read().splitlines()
yy3=open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/cross_validation_svm/extracted_features_sets/psi_blast/topo_sets/extracted_features_psi.topo','r').read().splitlines()
s4=open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/results/final_model_conservation.pred','r').read().splitlines()
yy4=open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/cross_validation_svm/extracted_features_sets/psi_blast/topo_sets/extracted_features_psi.topo','r').read().splitlines()

#........................order input..........................................

y=[]
y1=[]
tpl=zip(yy,s)
tpl.sort(key = operator.itemgetter(1),reverse = True)
for bla in tpl:
    y.append(int(bla[0]))
    y1.append(float(bla[1]))

y2=[]
y12=[]
tpl=zip(yy1,s1)
tpl.sort(key = operator.itemgetter(1),reverse = True)
for bla in tpl:
    y2.append(int(bla[0]))
    y12.append(float(bla[1]))
    
y3=[]
y13=[]
tpl=zip(yy2,s2)
tpl.sort(key = operator.itemgetter(1),reverse = True)
for bla in tpl:
    y3.append(int(bla[0]))
    y13.append(float(bla[1]))

y4=[]
y14=[]
tpl=zip(yy3,s3)
tpl.sort(key = operator.itemgetter(1),reverse = True)
for bla in tpl:
    y4.append(int(bla[0]))
    y14.append(float(bla[1]))

y5=[]
y15=[]
tpl=zip(yy4,s4)
tpl.sort(key = operator.itemgetter(1),reverse = True)
for bla in tpl:
    y5.append(int(bla[0]))
    y15.append(float(bla[1]))

#.........................roc_curve and roc_auc................................

y_true=np.array(y)
y_score=np.array(y1)
fpr, tpr, thresholds =roc_curve(y_true, y_score)
roc_auc = auc(fpr, tpr)

y_true2=np.array(y2)
y_score2=np.array(y12)
fpr2, tpr2, thresholds2 =roc_curve(y_true2, y_score2)
roc_auc2 = auc(fpr2, tpr2)

y_true3=np.array(y3)
y_score3=np.array(y13)
fpr3, tpr3, thresholds2 =roc_curve(y_true3, y_score3)
roc_auc3 = auc(fpr3, tpr3)

y_true4=np.array(y4)
y_score4=np.array(y14)
fpr4, tpr4, thresholds4 =roc_curve(y_true4, y_score4)
roc_auc4 = auc(fpr4, tpr4)

y_true5=np.array(y5)
y_score5=np.array(y15)
fpr5, tpr5, thresholds5 =roc_curve(y_true5, y_score5)
roc_auc5 = auc(fpr5, tpr5)

#...................ploting....................................................

plt.title('Receiver Operating Characteristic Default Radial Kernel and Optimized Radial Kernel')

#plt.plot(fpr, tpr, 'b',label='AUC set 5 = %0.2f'% roc_auc, color='c')
plt.plot(fpr2, tpr2, 'b',label='AUC Optimized Radial Kernel (c=8) = %0.2f'% roc_auc2, color='r')
plt.plot(fpr3, tpr3, 'b',label='AUC Default Radial kernel (c=0.546) = %0.2f'% roc_auc3, color='b')
plt.plot(fpr4, tpr4, 'b',label='AUC Default Radial Kernel with conservation = %0.2f'% roc_auc4, color='g')
plt.plot(fpr5, tpr5, 'b',label='AUC Optimized Radial Kernel with conservation = %0.2f'% roc_auc5, color='m')
plt.legend(loc='lower right')
plt.xlim([-0.0,1.01])
plt.ylim([-0.0,1.01])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()



