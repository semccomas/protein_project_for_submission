#created 29 Feb
#Sarah McComas
#last modified 1 March
#all files are in the same directory as point 1 unless otherwise specified

##### from point 1- opening a file to prepare for cd hit

f= open('membrane-alpha.3line', 'r')
aa= f.read().splitlines()
p=open('FASTA_format_for_cd_hit.txt','w')               #FASTA_format_for_cd_hit.txt will go into cd hit for processing. Output from cd hit would be called 'cd_hit_results_unsorted'

seq=[]
struc=[]
name=[]

for line in aa:
	if '>' in line:
		name.append(line)
	elif 'O' not in line:
		seq.append(line)
	else:
		struc.append(line)
zippy= zip(name, seq)
for a, b in zippy:
	p.write(a + '\n' + b + '\n')
p.close()

###### creating the dictionary#####


g= open('membrane-alpha.3line', 'r')
file=g.read().splitlines()

dic={}

for line in range(0, len(file), 3):
	dic[file[line]]= (file[line +1], file [line +2])



###### using the dictionary and cd hit output to read the file, separate every 50 sequences, and put into files point2TEST 1-7
### need to update for the 2nd '\n' in b.write and need to also figure out how to separate the two lines in the tuple


import re                          #to be used for multiple splits at once
file_counter = 1                 #to name the files in 'b'
counter=0                          #to count the number of sequences, when reaching 50 to start over

a= open ('cd_hit_result_unsorted.txt', 'r')
aread= a.read().splitlines()
b=open('./output/point2_output_1.txt','w')

for line2 in aread:                   #looking at the cd hit results line by line

	if "Cluster" not in line2:                          #ignoring the first line >Cluster 01 or whatever
		counter= counter + 1
		accession_names= re.split('... |	| ,' , line2)            #splitting, using re, by two values at once. This puts our name on its own
		dic_key=  accession_names[2]                                #accession_names 0= 0 or 1, 1= 234aa 2= >PWF23|2jf3B
		tuples=dic[dic_key]                           #this will be the sequence and structure (aka file[line +1 or +2])



		if accession_names[0]=='0' and counter >= 53:              #accession name =0 are all the lines that come directly at the start of the cluster
			file_counter= file_counter + 1 
			b= open('./output/point2_output_' + str(file_counter) + '.txt' , 'w')
			b.write(dic_key + '\n' + "%s\n%s\n" %tuples)                           #when the counter is over 50, open a new file and write to it
			print counter                                       #just a way to check that the counter is working properly. in our seq should see 50 appear 6 times
			counter =0                                    #have to restart the counter after so that it goes back to 50
		else:
			b.write(dic_key + '\n' + "%s\n%s\n" %tuples)         #see below

b.close



#as long as counter is under 50 and the accession number is not 0, it will write to the file you told it to open in the first 
#loop. B will get redefined when you reach over 50. That is how this can work. You have to define b before and 
#keep b in the loop when writing to it