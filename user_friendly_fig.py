import sys

script= sys.argv[0]
predicted_file= sys.argv[1]        #your classify output
original_file=sys.argv [2]      #your original sequence

predicted_file=open	(predicted_file, 'r').read().splitlines()
original_file= open (original_file , 'r').read().splitlines()

l= []
l2= []


for line2 in predicted_file:
	l2.append(line2)

for line in original_file:
	if '>' not in line:
		for wholeseq in line:
			for char in wholeseq:
				l.append(char) 

for (OG , pred) in zip (l, l2):
	#print OG , pred
	if '-' in pred:
		print OG, pred, ' not in membrane!'
	else:
		print OG, pred, 'membrane!!'

