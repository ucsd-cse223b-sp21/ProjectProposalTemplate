
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams['pdf.fonttype'] = 42


labels =  [ 'A', 'B', 'C', 'E', 'F']


default_means = [1,2,3,4,5]
control_means = [3,4,5,6,7]




x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects2 = ax.bar(x - width/2, default_means, width, label='System A',
        color='tab:red')
rects1 = ax.bar(x + width/2, control_means, width, label='System B', color='tab:blue', hatch='\\')


# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Y Label')
#ax.set_title('Clover YCSB-A (50% write)')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_xlabel("X Label")
ax.legend()


fig.tight_layout()
plt.savefig("example.pdf")
plt.show()
