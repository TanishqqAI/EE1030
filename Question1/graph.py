import matplotlib.pyplot as plt
import numpy as np

# Define the points
A = (1, -3)
B = (4, 5)
P = (2.125, 0)

# Define the line segment AB
x_values = np.linspace(1, 4, 100)
slope = (B[1] - A[1]) / (B[0] - A[0])
intercept = A[1] - slope * A[0]
y_values = slope * x_values + intercept

# Create the plot
fig, ax = plt.subplots(figsize=(10, 10))

# Plot the line segment AB
ax.plot(x_values, y_values, 'b-', linewidth=2, label='Line segment AB')

# Plot the points A, B, and P
ax.plot(A[0], A[1], 'ro', label='A(1, -3)')
ax.plot(B[0], B[1], 'ro', label='B(4, 5)')
ax.plot(P[0], P[1], 'ro', label='P(2.125, 0)')

# Annotate the points
ax.text(A[0], A[1], ' A(1, -3)', fontsize=12, verticalalignment='bottom', horizontalalignment='right', color='red')
ax.text(B[0], B[1], ' B(4, 5)', fontsize=12, verticalalignment='top', horizontalalignment='left', color='red')
ax.text(P[0], P[1], ' P(2.125, 0)', fontsize=12, verticalalignment='bottom', horizontalalignment='left', color='red')

# Set axis limits
ax.set_xlim(0, 5)
ax.set_ylim(-4, 6)

# Set ticks with 1 unit interval
ax.set_xticks(np.arange(0, 6, 1))
ax.set_yticks(np.arange(-4, 7, 1))

# Set labels and grid
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid(True, which='both', linestyle='-', linewidth=1, color='gray')  # Solid grey grid lines
ax.legend()

# Add the ratio annotation
ax.text(2.5, 2, 'Ratio 3:5', fontsize=12, color='green')

# Show the coordinate axes (spines)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# Ensure equal scaling for x and y axes
ax.set_aspect('equal')

plt.show()
