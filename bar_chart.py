import numpy as np
import matplotlib.pyplot as plt
 
# data to plot
n_groups = 7
benign = [2, 2, 4, 4, 5]
malicious = [6, 4, 5, 8, 8]
print(benign.__class__)
temp = benign + malicious
benign_bar = []
malicious_bar = []
for i in range(min(temp),max(temp)+1):
    benign_bar.append(benign.count(i))
    malicious_bar.append(malicious.count(i))
 
# create plot
#   fig, ax = plt.subplots()
index = np.arange(min(temp),max(temp)+1)
bar_width = 0.35
opacity = 0.8
 
rects1 = plt.bar(index, benign_bar, bar_width,
                 alpha=opacity,
                 color='g',
                 label='Benign')
 
rects2 = plt.bar(index + bar_width, malicious_bar, bar_width,
                 alpha=opacity,
                 color='r',
                 label='Mal')
 
plt.xlabel('Person')
plt.ylabel('Scores')
plt.title('Scores by person')
plt.xticks(index + bar_width/2, index)
#Chu thich
plt.legend()
 
plt.tight_layout()
plt.show()