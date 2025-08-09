import numpy as np 
import matplotlib.pyplot as plt 
from scipy.stats import pearsonr
from mpl_toolkits.mplot3d import Axes3D

np.random.seed(42)

# Generate spiral data
theta = np.linspace(0, 6 * np.pi, 800)
r = np.linspace(0, 50, 800) + np.random.normal(0, 2, 800)
z = np.linspace(-10, 10, 800)  # Ensure same length as x, y

x = r * np.cos(theta)
y = r * np.sin(theta)

# Pearson correlation between x and y
r_value, p_value = pearsonr(x, y)

# 3D Plot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
sc = ax.scatter(x, y,  c=theta, cmap='plasma', s=5, alpha=0.8)

plt.title(f'Pearson correlation coefficient: {r_value:.3f}')
plt.colorbar(sc, label='Z-axis Value')
plt.show()
