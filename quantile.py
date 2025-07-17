import numpy as np

data = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

q1 = np.quantile(data, 0.25)  # 25th percentile
q2 = np.quantile(data, 0.5)   # Median (50th percentile)
q3 = np.quantile(data, 0.75)  # 75th percentile

print("Q1 (25%):", q1)
print("Q2 (50% - Median):", q2)
print("Q3 (75%):", q3)
