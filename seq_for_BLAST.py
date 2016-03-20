#this processes all files from my database to make 313 individual files each with only one sequence 
#and a name. No structure. Counter is printed so you know how many files you should have

file_counter= 1
counter=0

a= open ('./membrane-alpha.3line', 'r')
afile= a.read().splitlines()
b=open('./FASTA_files/myseq_FASTA_1.txt','w')


for line in afile:
	if '>' in line:
		counter= counter +1
		file_counter= file_counter + 1 
		b= open('./FASTA_files/myseq_FASTA_' + str(file_counter) + '.txt' , 'w')
		b.write(line + '\n')
		print counter
	elif 'O' not in line:
		b.write(line)
	else:
		pass

b.close