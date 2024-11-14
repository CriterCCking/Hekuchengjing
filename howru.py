import numpy as np

import matplotlib.pyplot as plt

# Define the thumb coordinates
thumb_x = [0, 1, 2, 2.5, 2.7, 2.5, 2, 1, 0]
thumb_y = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4]

# Plot the thumb
plt.plot(thumb_x, thumb_y, 'b-', linewidth=3)

# Set the aspect of the plot to be equal
plt.gca().set_aspect('equal', adjustable='box')

# Add title and labels
plt.title('Thumbs Up')
plt.xlabel('X')
plt.ylabel('Y')

# Show the plot
plt.show()