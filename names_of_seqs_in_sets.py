g= open('../output/point2_BLAST_set6.txt', 'r')
g=g.read().splitlines()
s=open('./testingBLAST/BLAST_SVM_set6.txt', 'w')

count= 0
for line in g:
	count= count+1
	print line, count
	n=open(line).read()
	s.write(n+'\n')
s.close

