f = open('../output/topology.txt','r').read().splitlines()
f2 = open('../output/features_files/topology.fasta','w')
count=1
file_count = 0
for lines in f:
    count=count+1
    if count == 2:
        file_count = file_count + 1
        f2=open('../output/fasta_files/topology' + str(file_count) + '.fasta','w')
        f2.write(lines + '\n')
        count = 0
    else:
        f2.write(lines + '\n')


f2.close()

