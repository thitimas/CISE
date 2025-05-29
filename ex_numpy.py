import numpy as np

# 1. Create NumPy arrays
a = np.array([1, 2, 3])             # 1D array
b = np.array([[1, 2], [3, 4]])      # 2D array (matrix)

print("Array a:", a)
print("Array b:\n", b)

# 2. Array shape and size
print("Shape of b:", b.shape)       # (2, 2)
print("Size of a:", a.size)         # 3

# 3. Indexing and slicing
print("First element of a:", a[0])           # 1
print("Second row of b:", b[1])              # [3, 4]
print("Element at row 1, col 0 in b:", b[1, 0])  # 3

# 4. Array operations
c = a + 5                  # Add 5 to each element
d = a * 2                  # Multiply each element by 2
print("a + 5:", c)
print("a * 2:", d)

# 5. Element-wise operations
e = np.array([10, 20, 30])
print("a + e:", a + e)     # [11 22 33]
print("a * e:", a * e)     # [10 40 90]

# 6. Useful functions
print("Mean of a:", np.mean(a))
print("Sum of b:", np.sum(b))
print("Max of e:", np.max(e))

# 7. Reshape
f = np.array([1, 2, 3, 4, 5, 6])
f_reshaped = f.reshape((2, 3))
print("Reshaped f:\n", f_reshaped)

# 8. Zeros, ones, and random arrays
print("Zeros array:\n", np.zeros((2, 2)))
print("Ones array:\n", np.ones((2, 3)))
print("Random array:\n", np.random.rand(2, 3))


A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# 9. Matrix multiplication (dot product)
C = np.dot(A, B)

print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("A dot B:\n", C)


