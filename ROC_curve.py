from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
import random
import numpy as np 

########Single seq###########
file= open('./SVM/models_terminal_outputs_svm/ROC_single_seq_default_SORTED.txt', 'r').read().splitlines()
ilist= [ ]
for i in file:
	i= i.split('	')
	ilist.append(i)
myarray= np.asarray(ilist)
myarray= myarray.astype(np.float)
	
actual= myarray [ : , 0]
predictions= myarray [ : , 1 ]
print actual
print predictions
#print myarray
false_positive_rate, true_positive_rate, thresholds = roc_curve(actual, predictions)
roc_auc = auc(false_positive_rate, true_positive_rate)

#######KERNEL 0 ################
file0= open('./SVM_BLAST/testingBLAST/ROC_curve_kernel0_SORTED.txt', 'r').read().splitlines()
ilist0= [ ]
for i0 in file0:
	i0= i0.split('	')
	ilist0.append(i0)
myarray0= np.asarray(ilist0)
myarray0= myarray0.astype(np.float)
	
actual0= myarray0 [ : , 0]
predictions0= myarray0 [ : , 1 ]
print actual0
print predictions0

false_positive_rate0, true_positive_rate0, thresholds0 = roc_curve(actual0, predictions0)
roc_auc0 = auc(false_positive_rate0, true_positive_rate0)


##############KERNEL 2 ############
file2= open('./SVM_BLAST/testingBLAST/ROC_curve_kernel2_SORTED.txt', 'r').read().splitlines()
ilist2= [ ]
for i2 in file2:
	i2= i2.split('	')
	ilist2.append(i2)
myarray2= np.asarray(ilist2)
myarray2= myarray2.astype(np.float)
	
actual2= myarray2 [ : , 0]
predictions2= myarray2 [ : , 1 ]
print actual2
print predictions2
#print myarray
false_positive_rate2, true_positive_rate2, thresholds = roc_curve(actual2, predictions2)
roc_auc2 = auc(false_positive_rate2, true_positive_rate2)


#print true_positive_rate

plt.title('Receiver Operating Characteristic')
plt.plot(false_positive_rate, true_positive_rate, 'b', label='AUC for Single Sequence = %0.2f'% roc_auc)
plt.plot(false_positive_rate0, true_positive_rate0, 'b', color = 'red', label='AUC for MSA Linear Kernel = %0.2f'% roc_auc0)
plt.plot(false_positive_rate2, true_positive_rate2, 'b', color = 'black', label='AUC for MSA Radial Kernel = %0.2f'% roc_auc2)

plt.legend(loc='lower right')
plt.plot([0,1],[0,1],'r--')
plt.xlim([-0.1,1.2])
plt.ylim([-0.1,1.2])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
#plt.show()
plt.savefig('ROC_plot.png')