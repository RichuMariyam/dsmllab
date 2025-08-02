import numpy as np

# Input dimensions of Matrix A
rows_A = int(input("Enter number of rows for Matrix A: "))
cols_A = int(input("Enter number of columns for Matrix A: "))

# Input dimensions of Matrix B
rows_B = int(input("Enter number of rows for Matrix B: "))
cols_B = int(input("Enter number of columns for Matrix B: "))

# Check multiplication condition
if cols_A != rows_B:
    print(f"\n❌ Matrix multiplication NOT possible!")
    print(f"Number of columns in Matrix A ({cols_A}) must be equal to number of rows in Matrix B ({rows_B}).")
else:
    # Input Matrix A
    print("\nEnter elements of Matrix A:")
    A = []
    for i in range(rows_A):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        if len(row) != cols_A:
            print(f"Error: You must enter exactly {cols_A} elements.")
            exit()
        A.append(row)

    # Input Matrix B
    print("\nEnter elements of Matrix B:")
    B = []
    for i in range(rows_B):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        if len(row) != cols_B:
            print(f"Error: You must enter exactly {cols_B} elements.")
            exit()
        B.append(row)

    # Convert to NumPy arrays
    A = np.array(A)
    B = np.array(B)

    # Perform matrix multiplication
    C = np.dot(A, B)

    # Display results
    print("\nMatrix A:")
    print(A)

    print("\nMatrix B:")
    print(B)

    print("\nResult of Matrix Multiplication (A x B):")
    print(C)
