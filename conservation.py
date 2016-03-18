import pandas as pd
from math import log10
import sys


input_file1 = sys.argv[1]
input_file2 = sys.argv[2]
output_file = sys.argv[3]
#.................process psi-matrice................................


'''conservation=open(input_file1,'r')
ConservationFrame=pd.read_csv(conservation, engine='python')
normalization = lambda y : float(y/(log10(20) / log10(2)))
normalFrame = ConservationFrame.applymap(normalization)
d = map(list, normalFrame.values)


g=open(output_file,'w')

for lines in d:
    for i, c in enumerate(lines): 
        g.write(str(i+21) + ':' + str(c))
    g.write('\n')  
g.close()'''  
    
v=open(input_file1,'r').read().splitlines()
g=open(input_file2,'r').read().splitlines()
features_conservation_svm=open(output_file,'w')
result=zip(v,g)
for a,b in result:
    features_conservation_svm.write(str(a)+str(b)+'\n')
features_conservation_svm.close()