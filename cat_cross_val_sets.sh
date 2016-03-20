INPUT_DIR=/home/sarah/Desktop/prot.proj.scilifecomp/prot.proj/SVM_BLAST/testingBLAST

for i in $INPUT_DIR/BLAST_SVM_set*.txt; do
	for j in $INPUT_DIR/BLAST_SVM_set*.txt
	do
		base=`basename $i .txt`
		if [ $j = $INPUT_DIR/BLAST_SVM_set1.txt ]; then
			continue
		fi
		if [ $i = $INPUT_DIR/BLAST_SVM_set1.txt ]; then
			continue
		fi
		if [ $i != $j ];then
			cat $j >> $base.TRAIN.txt
		fi
	done
done
