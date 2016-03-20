#program for comparing the prediction results to MCC

import sys                          #to use for sys.argv[]
script_name= sys.argv[0]
input_file = sys.argv[1]            # so that you can only write 'python point1new.py input_file_name'
input_file_SVM= sys.argv[2]           #prediction_results
output_file= sys.argv[3]              #prediction_assessment2345
counts_file= sys.argv[4]

file=open(input_file)                  #need to open the input file
file_SVM= open(input_file_SVM)
fileread=file.read().splitlines()            #splitting to read line by line, will need in i1
file_SVM=file_SVM.read().splitlines()
o= open(output_file, 'w')
c=open(counts_file, 'w')


count=0
TN_count=0
TP_count=0
FN_count=0
FP_count=0
for a, b in zip (fileread, file_SVM):
	target_val= a[0]
	target_SVM= b[0]
	count= count+ 1
	p= '#' + str(count) + '\n'
	if target_val == '-' and target_SVM == '-':
		TN_count= TN_count + 1
		TN= 'TN '
		o.write(TN + p)

	elif target_val != '-' and target_SVM !='-':
		TP_count= TP_count + 1
		TP= 'TP '
		o.write(TP + p)

	elif target_val != '-' and target_SVM == '-':
		FN_count= FN_count + 1
		FN= 'FN '
		o.write(FN + p)

	elif target_val == '-' and target_SVM != '-':
		FP_count= FP_count + 1
		FP= 'FP '
		o.write(FP + p)

o.close

import math

MCC= (TP_count*TN_count - FP_count*FN_count)/ math.sqrt( (TP_count+FP_count)*(TP_count+FN_count)*(TN_count+FP_count)*(TN_count+FN_count))



c.write ('FN_count = '+ str(FN_count) + '\n' +'FP_count = '+ str(FN_count) + '\n' + 'TN_count = ' + str(TN_count) +'\n' + 'TP_count = ' + str(TP_count) + '\n' \
	'The MCC for: '+ output_file + '   is ' + str(MCC)  + '\n' + '\n' + "Does " + str(count) + '(number of lines in file)' + ' = ' + str(FN_count + FP_count + TN_count + TP_count) + ' (total TP,TN.. counts) ' + '?' )
c.close

print 'The MCC calculation, all TP, FP, TN, FN values, and the number of lines are printed in: ', counts_file

#print FN_count + FP_count + TN_count + TP_count
#print count
#print 'Do the above values match?'


#tp= TN.enumerate()
#print tp

# tp is true positives, fn is false negatives, etc


#this file seems to work. Double check that the FN and FP are supposed to be if the predictor is wrong 
#the SVM pred file is much longer, like thousands of characters longer. Do we care? 



#\text{MCC} = \frac{ TP \times TN - FP \times FN } {\sqrt{ (TP + FP) ( TP + FN ) ( TN + FP ) ( TN + FN ) } }
