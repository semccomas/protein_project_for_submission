script_file=/home/sarah/Desktop/prot.proj.scilifecomp/prot.proj/SVM/svm_light/
input_dir=/home/sarah/Desktop/prot.proj.scilifecomp/prot.proj/SVM_BLAST/testingBLAST
output_dir=/home/sarah/Desktop/prot.proj.scilifecomp/prot.proj/SVM_BLAST/testingBLAST/svm_classify_outputs

count=2
for i in $input_dir/BLAST_SVM_set*.TRAIN.txt ; do
base=`basename $i `
if [ -f $input_dir/model_KERNEL2-redo_$base ] ; then
	#$script_file./svm_learn -t 2 $i $output_dir/model_kernel2_$base
	$script_file./svm_classify $input_dir/BLAST_SVM_set$count.txt $input_dir/model_KERNEL2-redo_$base >$output_dir/accuracy_results_KERNEL2-redo_$count.txt $output_dir/predicted_results_KERNEL2_redo_$count.txt
	#echo $base
	#echo $output_dir/accuracy_results_set$count.txt
	let count=count+1
fi
done
