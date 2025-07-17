import matplotlib.pyplot as plt
import numpy as np

data = [10, 20, 15, 25, 30, 35, 25, 15, 50, 5]

plt.boxplot(data)
plt.title("Box Plot Example")
plt.ylabel("Values")
plt.grid(True)
plt.show()
