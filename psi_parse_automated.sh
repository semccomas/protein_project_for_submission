script_file=/home/sarah/Desktop/prot.proj.scilifecomp/prot.proj
input_dir=/home/sarah/Desktop/prot.proj.scilifecomp/prot.proj/outputs_BLAST
topology_dir=/home/sarah/Desktop/prot.proj.scilifecomp/prot.proj/FASTA_files/FASTA_struc
output_dir=/home/sarah/Desktop/prot.proj.scilifecomp/prot.proj/SVM_BLAST/

count=1
for i in $input_dir/*.psi ; do
base=`basename $i`
let count=count+1
if [ ! -f $output_dir/matrix_$count.txt ] ; then
	python $script_file/psi_parse_with_topology.py $input_dir/myseq_FASTA_$count.psi $topology_dir/mySTRUCTURE_FASTA_$count.txt $output_dir/matrix_$count.txt
	echo $count
fi
done
echo $count