from math import sqrt
import numpy as np
import matplotlib.pyplot as plt



target_value = open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/cross_validation_svm/extracted_features_sets/basic/6_sets/extracted_feature_set1.txt','r').read().splitlines()
target_pred = open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/cross_validation_svm/svm_models_pred/basic/prediction/set_1.pred','r').read().splitlines()
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
MCC1= (TP*TN - FN*FN) / sqrt( (TP + FP)*(TP + FN)*(TN + FP)*(TN + FN) )
        


target_value = open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/cross_validation_svm/extracted_features_sets/basic/6_sets/extracted_feature_set2.txt','r').read().splitlines()
target_pred = open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/cross_validation_svm/svm_models_pred/basic/prediction/set_2.pred','r').read().splitlines()
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
MCC2= (TP*TN - FN*FN) / sqrt( (TP + FP)*(TP + FN)*(TN + FP)*(TN + FN) )
        


target_value = open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/cross_validation_svm/extracted_features_sets/basic/6_sets/extracted_feature_set3.txt','r').read().splitlines()
target_pred = open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/cross_validation_svm/svm_models_pred/basic/prediction/set_3.pred','r').read().splitlines()
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
MCC3= (TP*TN - FN*FN) / sqrt( (TP + FP)*(TP + FN)*(TN + FP)*(TN + FN) )
        


target_value = open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/cross_validation_svm/extracted_features_sets/basic/6_sets/extracted_feature_set4.txt','r').read().splitlines()
target_pred = open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/cross_validation_svm/svm_models_pred/basic/prediction/set_4.pred','r').read().splitlines()
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
MCC4= (TP*TN - FN*FN) / sqrt( (TP + FP)*(TP + FN)*(TN + FP)*(TN + FN) )
        


target_value = open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/cross_validation_svm/extracted_features_sets/basic/6_sets/extracted_feature_set5.txt','r').read().splitlines()
target_pred = open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/cross_validation_svm/svm_models_pred/basic/prediction/set_5.pred','r').read().splitlines()
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

MCC5= (TP*TN - FN*FN) / sqrt( (TP + FP)*(TP + FN)*(TN + FP)*(TN + FN) )
        
print ([float(MCC1),float(MCC2),float(MCC3),float(MCC4),float(MCC5)])


#...........................................................................................................................................................


'''target_value = open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/cross_validation_svm/extracted_features_sets/psi_blast/extracted_features_psi1.svm','r').read().splitlines()
target_pred = open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/cross_validation_svm/svm_models_pred/psi_blast/prediction_psi/Kernel2/set1_psi_kernel2','r').read().splitlines()
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
MCCp1= (TP*TN - FN*FN) / sqrt( (TP + FP)*(TP + FN)*(TN + FP)*(TN + FN) )
        


target_value = open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/cross_validation_svm/extracted_features_sets/psi_blast/extracted_features_psi2.svm','r').read().splitlines()
target_pred = open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/cross_validation_svm/svm_models_pred/psi_blast/prediction_psi/Kernel2/set2_psi_kernel2','r').read().splitlines()
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
MCCp2= (TP*TN - FN*FN) / sqrt( (TP + FP)*(TP + FN)*(TN + FP)*(TN + FN) )
        


target_value = open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/cross_validation_svm/extracted_features_sets/psi_blast/extracted_features_psi3.svm','r').read().splitlines()
target_pred = open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/cross_validation_svm/svm_models_pred/psi_blast/prediction_psi/Kernel2/set3_psi_kernel2','r').read().splitlines()
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
MCCp3= (TP*TN - FN*FN) / sqrt( (TP + FP)*(TP + FN)*(TN + FP)*(TN + FN) )
        


target_value = open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/cross_validation_svm/extracted_features_sets/psi_blast/extracted_features_psi4.svm','r').read().splitlines()
target_pred = open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/cross_validation_svm/svm_models_pred/psi_blast/prediction_psi/Kernel2/set4_psi_kernel2','r').read().splitlines()
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
MCCp4= (TP*TN - FN*FN) / sqrt( (TP + FP)*(TP + FN)*(TN + FP)*(TN + FN) )
        


target_value = open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/cross_validation_svm/extracted_features_sets/psi_blast/extracted_features_psi5.svm','r').read().splitlines()
target_pred = open('/home/thomas/Desktop/19-02-2016-DSSPhelix-project/output/cross_validation_svm/svm_models_pred/psi_blast/prediction_psi/Kernel2/set5_psi_kernel2','r').read().splitlines()
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
MCCp5= (TP*TN - FN*FN) / sqrt( (TP + FP)*(TP + FN)*(TN + FP)*(TN + FN) )
        
print ([float(MCCp1),float(MCCp2),float(MCCp3),float(MCCp4),float(MCCp5)])'''




