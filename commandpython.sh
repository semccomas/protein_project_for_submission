#script_file=/home/sarah/Desktop/prot.proj.scilifecomp/prot.proj
input_dir=/home/sarah/Desktop/prot.proj.scilifecomp/prot.proj/output
#topology_dir=/home/sarah/Desktop/prot.proj.scilifecomp/prot.proj/FASTA_files/FASTA_struc
output_dir=/home/sarah/Desktop/prot.proj.scilifecomp/prot.proj/SVM_BLAST


for i in $input_dir/point2_BLAST_*.txt; do
	for j in $output_dir/SVM_BLAST_set*.txt; do
		if $i == $j 
	echo $i
done