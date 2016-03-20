import math
target_value = open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/cross_validation_svm/extracted_features_sets/psi_blast/topo_sets/extracted_features_psi2.topo','r').read().splitlines()
target_pred = open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/cross_validation_svm/svm_models_pred/psi_blast/prediction_psi/set2_c05_g2.pred','r').read().splitlines()
a=[]
b=[]
for target_score in target_value:
    a.append(target_score[0])
for score_pred in target_pred:
    b.append(score_pred[0])

TP = 1
FP = 1
TN = 1
FN = 1

    
for target, pred in zip(a,b):
    if target == '-' and pred == '-':
        TN = TN + 1
        
    elif target != '-' and pred != '-':
        TP = TP + 1
        
    elif target != '-' and pred == '-':
        FN = FN + 1
        
    elif target == '-' and pred != '-':
        FP = FP + 1
MCCp1= (TP*TN - FN*FN) / math.sqrt( (TP + FP)*(TP + FN)*(TN + FP)*(TN + FN) )
print 'MCC:',MCCp1

sensitivity = TP/float(TN+FP)
specificity = TN/float(TN+FP)

print 'sensitivity',sensitivity, 'specificity', specificity
