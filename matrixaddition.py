import numpy as np

# Get matrix size from user
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("\nEnter elements of Matrix A:")
A = []
for i in range(rows):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    A.append(row)

print("\nEnter elements of Matrix B:")
B = []
for i in range(rows):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    B.append(row)

# Convert to NumPy arrays
A = np.array(A)
B = np.array(B)

# Add the matrices
C = A + B

# Print results
print("\nMatrix A:\n", A)
print("\nMatrix B:\n", B)
print("\nSum of A and B:\n", C)
