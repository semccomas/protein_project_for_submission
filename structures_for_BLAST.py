#This processes all files from my database to make 313 individual files each with only one STRUCTURE
#and a name. No structure. Counter is printed so you know how many files you should have

#Same format as seq_for_blast just for structures


file_counter= 1
counter=0

a= open ('./membrane-alpha.3line', 'r')
afile= a.read().splitlines()
b=open('./FASTA_files/FASTA_struc/mySTRUCTURE_FASTA_1.txt','w')


for line in afile:
	if '>' in line:
		counter= counter +1
		file_counter= file_counter + 1 
		b= open('./FASTA_files/FASTA_struc/mySTRUCTURE_FASTA_' + str(file_counter) + '.txt' , 'w')
		b.write(line + '\n')
		print counter
	elif 'O' in line:
		b.write(line)
	else:
		pass

b.close