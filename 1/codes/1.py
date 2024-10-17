
from ctypes import *

# Load the shared object file (assuming it's already compiled as ratio.so)
ratio_lib = CDLL('./1.so')

# Prepare the arguments for the C function
x1 = c_float(1)  # Point A x-coordinate
y1 = c_float(-3) # Point A y-coordinate
x2 = c_float(4)  # Point B x-coordinate
y2 = c_float(5)  # Point B y-coordinate
k = c_float( )   # Variable to store the ratio

# Call the C function to calculate the ratio
ratio_lib.find_ratio(byref(x1), byref(y1), byref(x2), byref(y2), byref(k))

# Print the calculated ratio
print("The ratio in which the X-axis divides the line segment is: k = {:.2f}".format(k.value))
# Now visualize the result with Matplotlib
import numpy as np
import matplotlib.pyplot as plt

# Coordinates of the points A and B
A = np.array([1, -3])
B = np.array([4, 5])

# Find the intersection with the X-axis (y = 0)
P_x = A[0] + (B[0] - A[0]) * (-A[1]) / (B[1] - A[1])
P = np.array([P_x, 0])

# Plot the line segment and its division point on the X-axis
plt.figure()

# Plot points A, B, and the intersection point P
plt.scatter(*A, color='r', label='A(1, -3)')
plt.scatter(*B, color='g', label='B(4, 5)')
plt.scatter(*P, color='b', label=f'Intersection P({P[0]:.2f}, 0)')

# Plot the line segment AB
plt.plot([A[0], B[0]], [A[1], B[1]], color='r', label='Line AB')

# Plot the line from A and B to the intersection point
plt.plot([A[0], P[0]], [A[1], P[1]], color='gray', linestyle='dashed')
plt.plot([B[0], P[0]], [B[1], P[1]], color='gray', linestyle='dashed')

# Labeling the plot
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title('Line Segment AB and Intersection with X-axis')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)

plt.show()
