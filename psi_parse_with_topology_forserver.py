#created 7 March 2016. #edited for more trials 9 Mar and works great. Changed so that you don't have 2 outputs, just one
#Sarah McComas

import sys                          #to use for sys.argv[]
import numpy as np

script_name= sys.argv[0]                    
my_FASTA_psi = sys.argv[1]            # #p2o1my_BLAST264.txt for now.....
#structures= sys.argv[2]                   #/Users/semccomas/Desktop/prot.proj/FASTA_files/FASTA_struc/mySTRUCTURE_FASTA_264.txt for now...
cleaned_matrix= sys.argv[2]                   # ./SVM_BLAST/matrix264.txt for now.....  # will = output file


gread= open (my_FASTA_psi, 'r').read().splitlines()

bits2 = []
for line in gread[3:-6]:
	bits = line.split()
	bits = bits[2:22]
	bits2.append(bits)                          #making one long list so that you have a whole array not a bunch of values

myarray= np.asarray(bits2, dtype=float)
sigmoid= 1.0 / (1.0 + np.exp(-1.0 * myarray))

np.savetxt(cleaned_matrix, sigmoid, delimiter=' ')        
	
###############above cleans up the matrix, and calculates the sigmoidal function of the values##################

###############below takes the clean matrix, adds a header, the target value, and the PSSM #####################


r=open(cleaned_matrix, 'r')
rread= r.read().splitlines()
s=open(cleaned_matrix,'w')
#stru= open(structures, 'r').read().splitlines()


#s.write("# 'A':1, 'R':2, 'N':3, 'D':4, 'C':5, 'Q':6, 'E':7, 'G':8, 'H':9, 'I':10, 'L':11,\
#'K':12, 'M':13, 'F':14, 'P':15, 'S':16, 'T':17, 'W':18, 'Y':19, 'V':20" + '\n' + '\n')
#s.close

'''
top_list= []
for line2 in stru:
	if '>' not in line2:
		topology= line2
		for char in topology:
			if char =='M':
				#char = '1'
				top_list.append('1')
			else:
				#char= '-1'
				top_list.append('-1')
				'''

top_counter=0
counter=0
'''
for line3 in rread:
	listy=line3.split()
	s.write (str(top_list[top_counter]) + ' ')
	s.close
	top_counter= top_counter + 1
	'''
	
for line3 in rread:
	listy=line3.split()
	for char in listy:                             #listy is the whole array itself. This is how I can print the top_counter per amino acid
		counter= counter + 1                       #therefore char is just each PSSM for each aa in the actual seq
		s.write(str(counter) + ':'+ str(char) + ' ')
	counter=0                                       #the counter number matches the header above for the amino acid numbers
	s.close
	s.write('\n')
s.close

'''
if len(top_list) != top_counter:
	print 'Error: structure file does not match BLAST output!'
	#####You might never get this message because it will probably say: s.write (str(top_list[top_counter]) + ' ')
	######  IndexError: list index out of range
else:
	print 'Structure files and BLAST output length are the same:' , len(top_list) , '!!'
'''

