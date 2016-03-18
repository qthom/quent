x=open('../output/formated_cluster.txt', 'w')
l=[]
the_file_lines = open('../input/cd_hit_files/1456834993.fas.1.clstr', 'r').read().splitlines()
line=the_file_lines.pop()
for line in the_file_lines:
    i=line[0]
    if '>' not in i:
        l.append(line)
    else:
        None
  
for each in l:
   
    e=str(each)
    x.write(e+'\n')

