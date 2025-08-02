import numpy as np

# Input size of vectors
n = int(input("Enter the number of elements in the vectors: "))

# Input Vector A
print("Enter elements of Vector A separated by spaces:")
A = list(map(float, input().split()))
if len(A) != n:
    print(f"Error: You must enter exactly {n} elements.")
    exit()

# Input Vector B
print("Enter elements of Vector B separated by spaces:")
B = list(map(float, input().split()))
if len(B) != n:
    print(f"Error: You must enter exactly {n} elements.")
    exit()

# Convert to numpy arrays
A = np.array(A)
B = np.array(B)

# Calculate dot product
dot_product = np.dot(A, B)

print(f"\nVector A: {A}")
print(f"Vector B: {B}")
print(f"Dot Product: {dot_product}")
