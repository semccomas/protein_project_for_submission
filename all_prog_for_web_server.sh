


script_dir=/home/sarah/Desktop/prot.proj.scilifecomp/prot.proj   #here we are using psi_parse_with_topology , 
input_dir=/home/sarah/Desktop/prot.proj.scilifecomp/prot.proj/webserver  #here we will make wherever you're getting your sequence from
blast_dir=/home/sarah/Desktop/prot.proj.scilifecomp/prot.proj/webserver #here will be the output for where you want your blast files to go. 
output_dir=/home/sarah/Desktop/prot.proj.scilifecomp/prot.proj/webserver
svm_dir=/home/sarah/Desktop/prot.proj.scilifecomp/prot.proj/SVM/svm_light/
model_dir=/home/sarah/Desktop/prot.proj.scilifecomp/prot.proj/SVM_BLAST/testingBLAST #in here we have the 3rd

##### STEP 1- RUN BLAST ##### 

for i in $input_dir/myseq_FASTA_15.fasta; do          #like f below in step 2, you have to change this when it's actually time to run
	base= `basename $i`
	echo $base
#	blastpgp -i $i -j 3 -d $database_file -i $i -o $blast_dir/$base.blastpgp -Q $blast_dir/$base.psi
done

#step 1- run blast on file. This is just using the default settings from sarahblast.sh so i think it'll be the same



#######STEP 2- MATRIX PARSING####### 
for f in $script_dir/myseq_FASTA_15_TESTforserver.txt; do     #this will become blast_dir/$base.psi. for now we pretend this 15 file is our blast output (is just a copy from the psi file)
python $script_dir/psi_parse_with_topology_forserver.py $f $blast_dir/matrix_SERVERTEST.txt
	done
#so this step parses the psiblast output. The psiparse file is the same exact file as the original psi_parse but does NOT include stuctures and target values.


#####STEP 3- SVM CLASSIFY ######### 
for g in $blast_dir/matrix_SERVERTEST.txt; do   #notice that as in f above, g is the output of the previous step
$svm_dir./svm_classify $g $model_dir/model_c-0.5_w-0.5_ALLSEQS_BLAST_SVM_all5.txt >$output_dir/accuracy_results_TEST_SERVER.txt $output_dir/predicted_results_TEST_SERVER.txt
done 
#and then from here we will run classify on it. First tested on (first variable after classify) is output from matrix parsed
#model will be whatever you want it to be. here i choose one that is used for all 5 sets against set 1 and is optimized.





############# I don't think you can calculate the MCC because you don't have target values as before #########
###STEP 4- MAKING A USER FRIENDLY MODEL ##############
for h in $output_dir/predicted_results_TEST_SERVER.txt; do
	python $script_dir/user_friendly_fig.py $h $i    # $i = ./FASTA_files/myseq_FASTA_15.txt here
done
