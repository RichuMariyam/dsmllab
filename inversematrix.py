import numpy as np

# Input size of square matrix
n = int(input("Enter the size of the square matrix (n x n): "))

# Input matrix elements
print(f"Enter the elements of the {n}x{n} matrix row-wise:")

matrix = []
for i in range(n):
    row = list(map(float, input(f"Row {i+1}: ").split()))
    if len(row) != n:
        print(f"Error: You must enter exactly {n} elements.")
        exit()
    matrix.append(row)

# Convert to NumPy array
matrix = np.array(matrix)

# Check if matrix is invertible (determinant != 0)
det = np.linalg.det(matrix)
print(f"\nDeterminant: {det}")

if det == 0:
    print("Matrix is singular and does NOT have an inverse.")
else:
    inv_matrix = np.linalg.inv(matrix)
    print("\nInverse of the matrix:")
    print(inv_matrix)
