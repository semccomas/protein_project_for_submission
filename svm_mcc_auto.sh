script_file=/home/sarah/Desktop/prot.proj.scilifecomp/prot.proj/SVM_BLAST/testingBLAST
input_dir_OG_set=/home/sarah/Desktop/prot.proj.scilifecomp/prot.proj/SVM_BLAST/testingBLAST
input_dir_SVM=/home/sarah/Desktop/prot.proj.scilifecomp/prot.proj/SVM_BLAST/testingBLAST/svm_classify_outputs
output_dir_TP_TN=/home/sarah/Desktop/prot.proj.scilifecomp/prot.proj/SVM_BLAST/testingBLAST/MCCs
output_dir_MCC_num=/home/sarah/Desktop/prot.proj.scilifecomp/prot.proj/SVM_BLAST/testingBLAST/MCCs


#script_file=/Users/semccomas/Desktop/prot.proj/SVM_BLAST/testingBLAST
#input_dir_OG_set=/Users/semccomas/Desktop/prot.proj/SVM/svm_input
#input_dir_SVM=/Users/semccomas/Desktop/prot.proj/SVM/models_terminal_outputs_svm
#output_dir_TP_TN=/Users/semccomas/Desktop/prot.proj/SVM
#output_dir_MCC_num=/Users/semccomas/Desktop/prot.proj/SVM

count=2
for i in $input_dir_OG_set/BLAST_SVM_set?.txt ; do           #here this will be BLAST_SVM_set2.txt
base=`basename $i `                                                 #base= point1_output2 here.
#for j in $input_dir_SVM/predicted_results_set?.txt; do
if [ -f $input_dir_SVM/predicted_results_set$count.txt ] ; then              #here this will be predicted_results2.txt
	#echo $base
	#echo $j
	python $script_file/svm_pred_MCC.py $input_dir_OG_set/BLAST_SVM_set$count.txt $input_dir_SVM/predicted_results_set$count.txt $output_dir_TP_TN/TN_TP_listed_set$count.txt $output_dir_MCC_num/mcc_num_set$count.txt        #the last one will be the same as you have in the machine. TP_TN output will be called TNTP comparison
	let count=count+1
	fi
done

#echo $base