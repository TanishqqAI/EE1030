from ctypes import *

# Load the shared object file (make sure it's in the same directory as the script)
ratio_lib = CDLL('./1.so')

# Define the function signatures for the C functions used
ratio_lib.createMat.argtypes = [c_int, c_int]
ratio_lib.createMat.restype = POINTER(POINTER(c_double))

ratio_lib.Matsec.argtypes = [POINTER(POINTER(c_double)), POINTER(POINTER(c_double)), c_int, c_double]
ratio_lib.Matsec.restype = POINTER(POINTER(c_double))

ratio_lib.freeMat.argtypes = [POINTER(POINTER(c_double)), c_int]

# Prepare the arguments for points A and B
# Create matrices for A and B
A = ratio_lib.createMat(2, 1)
B = ratio_lib.createMat(2, 1)

# Set coordinates for points A(1, -3) and B(4, 5)
A[0][0] = c_double(1)
A[1][0] = c_double(-3)

B[0][0] = c_double(4)
B[1][0] = c_double(5)

# Calculate the ratio k
k = -A[1][0] / (B[1][0])
print("The ratio in which the X-axis divides the line segment is: k = {:.2f}".format(k))

# Calculate the intersection point using Matsec
P = ratio_lib.Matsec(A, B, 2, k)

# Print the point of intersection
print("The point of intersection with the X-axis is: (%.2f, %.2f)" % (P[0][0], P[1][0]))

# Free allocated memory
ratio_lib.freeMat(A, 2)
ratio_lib.freeMat(B, 2)
ratio_lib.freeMat(P, 2)

# Now visualize the result with Matplotlib
import numpy as np
import matplotlib.pyplot as plt

# Coordinates of points A and B
A_coords = np.array([A[0][0], A[1][0]])
B_coords = np.array([B[0][0], B[1][0]])

# Intersection point
P_coords = np.array([P[0][0], P[1][0]])

# Plot the line segment and its division point on the X-axis
plt.figure()

# Plot points A, B, and the intersection point P
plt.scatter(*A_coords, color='r', label='A(1, -3)')
plt.scatter(*B_coords, color='g', label='B(4, 5)')
plt.scatter(*P_coords, color='b', label=f'Intersection P({P_coords[0]:.2f}, 0)')

# Plot the line segment AB
plt.plot([A_coords[0], B_coords[0]], [A_coords[1], B_coords[1]], color='r', label='Line AB')

# Plot the dashed lines from A and B to the intersection point
plt.plot([A_coords[0], P_coords[0]], [A_coords[1], P_coords[1]], color='gray', linestyle='dashed')
plt.plot([B_coords[0], P_coords[0]], [B_coords[1], P_coords[1]], color='gray', linestyle='dashed')

# Labeling the plot
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title('Line Segment AB and Intersection with X-axis')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)

plt.show()
