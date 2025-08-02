import numpy as np

# Get matrix size
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Input Matrix A
print("\nEnter elements of Matrix A:")
A = []
for i in range(rows):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    A.append(row)

# Input Matrix B
print("\nEnter elements of Matrix B:")
B = []
for i in range(rows):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    B.append(row)

# Convert to numpy arrays
A = np.array(A)
B = np.array(B)

# Subtract matrices
C = A - B

# Show results
print("\nMatrix A:\n", A)
print("\nMatrix B:\n", B)
print("\nSubtraction (A - B):\n", C)
