import sys                          #to use for sys.argv[]
script_name= sys.argv[0]
membrane_3line = sys.argv[1]            # ./membrane-alpha.3line
cluster= sys.argv[2]             # ./output/point2_output_1.txt'
out= sys.argv[3]                #./output/point2_BLAST_set1.txt


fread= open(membrane_3line, 'r').read().splitlines()
cluster=  open(cluster, 'r').read().splitlines()
out= open(out, 'w')


seqcount= 1 
name_dic={}

for line in fread:
	if '>' in line:
		membname= line
		seqcount= seqcount+1
		name_dic[membname]= ('matrix_' + str(seqcount) + '.txt')

for acc in cluster:
	if acc in name_dic:
		out.write(name_dic[acc] + '\n')
		#print name_dic[acc]
		#p2o1new.write (acc + '	' + name_dic[acc] + '\n')

out.close


