l=[]
u=[]
nb='1234567890'
the_file_lines = open('../input/cd_hit_results/1456734427.fas.1.clstr.sorted', 'r').read().splitlines()
other_lines=the_file_lines.pop()
each_lines=the_file_lines.pop()
for each_lines in the_file_lines:
    i=each_lines[0]
    c=each_lines[6]
    if '>' not in i:
        l.append(i+each_lines[8:29])
x=open('../output/wrong_format.txt', 'w')
for string in l:
    if '>' not in string:
        True
    if '\t' in string:
        True
    if True:
        x.write(string+'\n')

new_file=open('../output/wrong_format.txt','r').read().splitlines()
l2=[]
for line in new_file:
    if ' ' in line:
        line.replace(' ','')
    if ',' in line:
        line.replace(',','')
    if ', ' in line:
        line.replace(', ','')
    if '...' in line:
        line.replace('...','')
    if '..' in line:
        line.replace('..','')
    print line
    