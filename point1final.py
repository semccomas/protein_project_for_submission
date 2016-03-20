#point 1 in project--- date modified: 2016-03-01 
#Sarah McComas

import sys                          #to use for sys.argv[]
script_name= sys.argv[0]
input_file = sys.argv[1]            # so that you can only write 'python point1new.py input_file_name'
output_file= sys.argv[2]
i=open(input_file)                  #need to open the input file
aa=i.read().splitlines()            #splitting to read line by line, will need in aa
o= open(output_file, 'w')

header= "######'A':1, 'R':2, 'N':3, 'D':4, 'C':5, 'Q':6, 'E':7, 'G':8, 'H':9, 'I':10, 'L':11,\
'K':12, 'M':13, 'F':14, 'P':15, 'S':16, 'T':17, 'W':18, 'Y':19, 'V':20"
o.write (header + '\n')
o.close

name= []                    #should print the first name as it looks like in fasta
seq_list= []                   #will hold the list of the amino acids as a string
struct_list= []                 #will hold a list of the structure letters I, M, or O as a string
target=[]                   #will use to print -1 or 1 for the target values. -1 for all non M's, 1 for M
amino_numbs= []             # will compile a list of all numbers referred to by the dictionary below

amino= {'A':1, 'R':2, 'N':3, 'D':4, 'C':5, 'Q':6, 'E':7, 'G':8, 'H':9, 'I':10, 'L':11,\
'K':12, 'M':13, 'F':14, 'P':15, 'S':16, 'T':17, 'W':18, 'Y':19, 'V':20}


for line in aa:
	if '>' in line:
		name.append(line)     #making a list of all fasta format names
	elif 'O' not in line:
		seq_list.append(line)       #making a list of amino acids by letter name. Since line is a whole line this turns into a string
	else:
		struct_list.append(line)     #see above but for structures I, M, O


for amino_string in seq_list:                     #this double loop and the set below are solving the same problem- a list of a line as a strings
	for single_amino in amino_string:
		amino_numbs.append(amino[single_amino])        #referring to the dict that will then print numbers instead of letters. Numbers are arbitrary


for struct_string in struct_list:      
	for single_struct in struct_string:               #as above, otherwise python evaluated 'IOOOMMMMOOOOOIII' as one entity and obviously that does not == "M"
		if single_struct=='M':
			target.append(1)                       #the value in feature:value will always be 1 here since we did not account for non present aa's.
		else:                                      # only M dictates what target value will be 
			target.append (-1)


zippy= zip(target, amino_numbs)
for a, b in zippy:
	o.write(str(a)+ ' ' + str(b) + ':1\n')

o.close           



	#we assign a 1 because we chose not to print out a 0 for each amino acid that is not there. We will need
	#to do this in PSIBLAST so check out 'point1new.py' where I left the code intact considering what you would 
	#do with a 0. It is not complete but it's the start of an idea
