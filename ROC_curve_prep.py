#this will cat the 5 sets together. sort based on prediction tv's and then be ready to input to the ROC curve

import operator as op

############ FOR SINGLE SEQ ###############
'''
filenames_SVM = ['./SVM/models_terminal_outputs_svm/prediction_results2345_NEW.txt', './SVM/models_terminal_outputs_svm/prediction_results2346_NEW.txt', './SVM/models_terminal_outputs_svm/prediction_results2356.txt', './SVM/models_terminal_outputs_svm/prediction_results2456.txt', './SVM/models_terminal_outputs_svm/prediction_results3456.txt']
with open('./SVM/models_terminal_outputs_svm/ALL_predicted_results.txt', 'w') as outfile_SVM:
    for fname in filenames_SVM:
        with open(fname) as infile:
            for line in infile:
                outfile_SVM.write(line)
outfile_SVM.close


filenames_actual = ['./SVM/svm_input/point1_output6.txt', './SVM/svm_input/point1_output5.txt', './SVM/svm_input/point1_output4.txt', './SVM/svm_input/point1_output3.txt', './SVM/svm_input/point1_output2.txt']
with open('./SVM/models_terminal_outputs_svm/ALL_actual_results.txt', 'w') as outfile_actual:
    for fname2 in filenames_actual:
        with open(fname2) as infile2:
            for line2 in infile2:
            	line2=str(line2).split()
            	#line2=[line2]
                outfile_actual.write(line2[0]+'\n')
outfile_actual.close
 


###### FOR MULTI SEQ ##############
filenames_SVM = ['predicted_results_KERNEL2_2.txt', 'predicted_results_KERNEL2_3.txt', 'predicted_results_KERNEL2_4.txt', 'predicted_results_KERNEL2_5.txt', 'predicted_results_KERNEL2_6.txt']
with open('./SVM_BLAST/testingBLAST/ALL_predicted_results_kernel2.txt', 'w') as outfile_SVM:
    for fname in filenames_SVM:
        with open(fname) as infile:
            for line in infile:
                outfile_SVM.write(line)
outfile_SVM.close


filenames_actual = ['./SVM_BLAST/testingBLAST/BLAST_SVM_set2.txt', './SVM_BLAST/testingBLAST/BLAST_SVM_set3.txt', './SVM_BLAST/testingBLAST/BLAST_SVM_set4.txt', './SVM_BLAST/testingBLAST/BLAST_SVM_set5.txt', './SVM_BLAST/testingBLAST/BLAST_SVM_set6.txt']
with open('./SVM_BLAST/testingBLAST/ALL_actual_results_kernel2.txt', 'w') as outfile_actual:
    for fname2 in filenames_actual:
        with open(fname2) as infile2:
            for line2 in infile2:
            	line2=str(line2).split()
            	#line2=[line2]
                outfile_actual.write(line2[0]+'\n')
outfile_actual.close

'''


############multi seq Kernel 0 ###########

filenames_SVM = ['./SVM_BLAST/testingBLAST/svm_classify_outputs/predicted_results_KERNEL0_BLAST_SVM_set2.TRAIN.txt', './SVM_BLAST/testingBLAST/svm_classify_outputs/predicted_results_KERNEL0_BLAST_SVM_set3.TRAIN.txt', './SVM_BLAST/testingBLAST/svm_classify_outputs/predicted_results_KERNEL0_BLAST_SVM_set4.TRAIN.txt', './SVM_BLAST/testingBLAST/svm_classify_outputs/predicted_results_KERNEL0_BLAST_SVM_set5.TRAIN.txt', './SVM_BLAST/testingBLAST/svm_classify_outputs/predicted_results_KERNEL0_BLAST_SVM_set6.TRAIN.txt']
with open('./SVM_BLAST/testingBLAST/ALL_predicted_results_kernel0.txt', 'w') as outfile_SVM:
    for fname in filenames_SVM:
        with open(fname) as infile:
            for line in infile:
                outfile_SVM.write(line)
outfile_SVM.close


filenames_actual = ['./SVM_BLAST/testingBLAST/BLAST_SVM_set2.txt', './SVM_BLAST/testingBLAST/BLAST_SVM_set3.txt', './SVM_BLAST/testingBLAST/BLAST_SVM_set4.txt', './SVM_BLAST/testingBLAST/BLAST_SVM_set5.txt', './SVM_BLAST/testingBLAST/BLAST_SVM_set6.txt']
with open('./SVM_BLAST/testingBLAST/ALL_actual_results_kernel0.txt', 'w') as outfile_actual:
    for fname2 in filenames_actual:
        with open(fname2) as infile2:
            for line2 in infile2:
            	line2=str(line2).split()
            	#line2=[line2]
                outfile_actual.write(line2[0]+'\n')
outfile_actual.close




