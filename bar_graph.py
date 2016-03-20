import numpy as np
import matplotlib.pyplot as plt


n_groups = 3

'''

means_men = (20, 35, 30)
std_men = (2, 3, 4)

means_women = (25, 32, 34)
std_women = (3, 5, 2)

'''

accuracy= (0.6364, 0.7335, 0.7666)
MCC= (0.1267, 0.4735, 0.5038)

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.35

opacity = 0.7
#error_config = {'ecolor': '0.3'}

rects1 = plt.bar(index, accuracy, bar_width,
                 alpha=opacity,
                 color='r',
                 #yerr=accuracy,
 #                error_kw=error_config,
                 label='Accuracy')

rects2 = plt.bar(index + bar_width, MCC, bar_width,
                 alpha=opacity,
                 color='c',
                 #yerr=MCC,
  #               error_kw=error_config,
                 label='MCC Value')

plt.xlabel('SVM Model')
plt.ylabel('Accuracy and MCC')
plt.title('Predictor Quality for Several Models')
plt.xticks(index + bar_width, ('Single Sequence', 'MSA Linear Kernel ', 'MSA Radial Kernel'))
plt.legend()
plt.tight_layout()

plt.ylim((0,1))

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%s' % float(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

#plt.show()
plt.savefig('bar_graph_fig2.png')