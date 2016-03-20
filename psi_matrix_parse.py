#created 7 March 2016. #edited for more trials 9 Mar and works great. Changed so that you don't have 2 outputs, just one
#Sarah McComas

import sys                          #to use for sys.argv[]
script_name= sys.argv[0]                    
my_FASTA_psi = sys.argv[1]            # #p2o1my_BLAST264.txt for now.....
cleaned_matrix= sys.argv[2]                   # ./SVM_BLAST/psi_clean_matrix264.txt for now.....


#cleaned_matrix_with_feat= sys.argv[3]     #./SVM_BLAST/psi_clean_with_feat264.txt for now.....



g= open (my_FASTA_psi, 'r')
gread= g.read().splitlines()

import numpy as np 

bits2 = []

for line in gread[3:-6]:
	bits = line.split()
	bits = bits[2:22]
	bits2.append(bits)                          #making one long list so that you have a whole array not a bunch of values

myarray= np.asarray(bits2, dtype=float)
sigmoid= 1.0 / (1.0 + np.exp(-1.0 * myarray))

np.savetxt(cleaned_matrix, sigmoid, delimiter=' ')        
	
######above cleans up the matrix, and calculates the sigmoidal function of the values###


r=open(cleaned_matrix, 'r')
rread= r.read().splitlines()
s=open(cleaned_matrix,'w')

counter=0
s.write("# 'A':1, 'R':2, 'N':3, 'D':4, 'C':5, 'Q':6, 'E':7, 'G':8, 'H':9, 'I':10, 'L':11,\
'K':12, 'M':13, 'F':14, 'P':15, 'S':16, 'T':17, 'W':18, 'Y':19, 'V':20" + '\n' + '\n')
s.close

for lines in rread:
	listy=lines.split()
	for char in listy:
		counter= counter + 1
		s.write(str(counter) + ':'+ str(char) + ' ')
	counter=0                                       #the counter number matches the header above for the amino acid numbers
	s.close
	s.write('\n')
s.close


####above adds the amino number (feature number) to the value ###########