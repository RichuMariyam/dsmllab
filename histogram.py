import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)  # 1000 normally distributed random numbers

plt.hist(data, bins=30, color='purple', edgecolor='black')
plt.title("Histogram Example")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()
