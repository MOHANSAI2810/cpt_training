import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Patch

data = ['a', 'b', 'c']
v1 = [5, 10, 15]
v2 = [8, 12, 10]

x = np.arange(len(data))  # x positions
y = np.zeros(len(data))   # y positions (since bars are aligned)
z = np.zeros(len(data))   # starting z position for first set

width = 0.5
depth = 0.5

np.random.seed(42)
colors = plt.cm.tab10(np.random.rand(2))

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# First set of bars at z=0
ax.bar3d(x, y, z, width, depth, v1, color=colors[0], edgecolor='black', alpha=0.8, label='Dataset 1')

# Second set of bars stacked on top of first (z = v1 heights)
ax.bar3d(x, y, v1, width, depth, v2, color=colors[1], edgecolor='black', alpha=0.8, label='Dataset 2')

ax.set_xticks(x + width / 2)
ax.set_xticklabels(data)
ax.set_xlabel('Data')
ax.set_ylabel('Y')
ax.set_zlabel('Values')
ax.set_title('3D Stacked Bar Chart')

legend_patches = [Patch(color=colors[0], label='Dataset 1'),Patch(color=colors[1], label='Dataset 2')]
ax.legend(handles=legend_patches)

plt.tight_layout()
plt.show()
