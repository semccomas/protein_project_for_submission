
input_dir=/home/sarah/Desktop/prot.proj.scilifecomp/prot.proj/outputs


for i in $input_dir/point2_BLAST_*.txt; do
	for j in $i; do
		echo $j
	done
