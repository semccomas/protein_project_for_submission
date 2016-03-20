# protein_project_for_submission
Here is information on each program that I have submitted for ease of nagivation:
It is worth noting that because I was only able to ssh in to my machine and not actually sit at the desk,
some programs are written for my own computer and thus the directories are different


point1final.py ---> extract features from the database membrane-alpha.3line and append target values based on structure

point2new.py ---> creating a list of FASTA files for entry into CD-HIT and then creating 6 cross validation sets from the CD HIT output

seq_for_BLAST.py ---> separating all 313 sequences from the database into individual files to be used while running PSIBLAST

sarahblast.sh ---> automating the BLAST running process for all files that came from seq_for_BLAST.py

cat_cross_val_sets.sh ---> creating the cross validation sets and using set1 as my validation set for final optimization

structures_for_BLAST.py --> as seq_for_BLAST, I made 313 files of all the structure so that I could append the target values properly to the BLAST output for the 
corresponding sequence and use them in psi_parse*

psi_parse_automated.sh ---> automate the psi_parse_with_topology.py program for all 313 sequences

psi_parse_with_topology.py ---> takes the structures from structures_for_BLAST.py and the blast output files and transforms the PSSM from blast to 
be 0-1 with the sigmoid function. Appends the corresponding target value to each line and add an amino acid number 1-20 to each value in the sequence

BLAST_to_SVM_sets.py ---> print the filename (1-313) for each sequence that belonged to a certain cross validation set. This along with 
names_of_seqs_in_sets.py put together the BLAST output files (parsed by psi_parse) to be in the proper cross validation sets as created by point2new.py 

names_of_seqs_in_sets.py ---> took the output from BLAST_to_SVM_sets.py and concatenated the contents (BLAST outputs) to the proper cross validation sets

svm_automated.sh ---> running SVM learn and SVM classify automatically. I would simply comment out either learn or classify depending on which I wanted to run 
and change the output directory. I would also just change the model names  based on what kernel and parameters I was running. 

svm_pred_MCC.py ---> calculate the MCC for each classifier output

svm_mcc_auto.sh ---> automate svm_pred_MCC so it would run for all 5 cross validation sets 

ROC_curve_prep.py ---> This, along with two bash lines (paste and sort -k2 -r -n <filename>) to concatanate all files for a given cross validation
set model and sort it for reading into the ROC curve.

ROC_curve.py ---> actually generating the ROC curve

bar_graph.py ---> generating a bar graph for the average values of several notable predictors 

