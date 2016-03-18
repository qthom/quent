#Created 05/03/2016 by Quentin Thomas
#Extraction features from sequences and structure
#Modified last 07/03/2016
import pandas as pd
from math import exp
import sys


input_file = sys.argv[1]
output_file = sys.argv[2]


w=open(output_file, 'w')
DataFrame=pd.read_csv(input_file,engine='python', sep=' ', header=0, names=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'])
proba = lambda x : float(1/(1+exp(-x)))
ProbaFrame = DataFrame.applymap(proba)
b = map(list, ProbaFrame.values)
for line in b:
    for i, c in enumerate(line):
        w.write(str(i+1) + ':' + str(c) + ' ')
    w.write('\n')
        