import numpy as np
import matplotlib.pyplot as plt

# Create some sample data points for the vectors
x = np.linspace(-2, 2, 10)
y = np.linspace(-2, 2, 10)
X, Y = np.meshgrid(x, y)

# Define vector components (u and v) for the vectors
u = X
v = Y

# Define which vectors to highlight in red and blue
highlight_indices_red = [(3, 3), (4, 4)]  # Indices of vectors to highlight in red
highlight_indices_blue = [(6, 6), (7, 7)]  # Indices of vectors to highlight in blue

# Create a plot
plt.figure()

# Plot all vectors in gray
plt.quiver(X, Y, u, v, color='gray', angles='xy', scale_units='xy', scale=1, label='Gray Vectors')

# Plot the vectors to highlight in red
for i, j in highlight_indices_red:
    plt.quiver(X[i, j], Y[i, j], u[i, j], v[i, j], color='red', angles='xy', scale_units='xy', scale=1, label='Red Vectors')

# Plot the vectors to highlight in blue
for i, j in highlight_indices_blue:
    plt.quiver(X[i, j], Y[i, j], u[i, j], v[i, j], color='blue', angles='xy', scale_units='xy', scale=1, label='Blue Vectors')

# Set plot limits and labels
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Add a legend
plt.legend()

# Show the plot
plt.show()
