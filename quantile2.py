import numpy as np
import matplotlib.pyplot as plt

data = np.array([10,20,30,40,50,60,70,80,90,100])
q1, q2, q3 = np.quantile(data, [0.25, 0.5, 0.75])

plt.hist(data, bins=10, edgecolor='black')
for q, c, l in zip([q1, q2, q3], ['green','red','purple'], ['Q1','Median','Q3']):
    plt.axvline(q, color=c, linestyle='--', label=l)

plt.legend()
plt.show()
