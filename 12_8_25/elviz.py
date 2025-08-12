import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2*np.pi, 400)

# Lasso: L1 norm constraint (diamond)
lasso_x = np.cos(theta) / (np.abs(np.cos(theta)) + np.abs(np.sin(theta)))
lasso_y = np.sin(theta) / (np.abs(np.cos(theta)) + np.abs(np.sin(theta)))

# Ridge: L2 norm constraint (circle)
ridge_x = np.cos(theta)
ridge_y = np.sin(theta)

# Elastic Net: Combination, here weighted sum of L1 and L2 norms
alpha = 0.5  # mixing parameter between lasso and ridge
elastic_x = alpha * lasso_x + (1 - alpha) * ridge_x
elastic_y = alpha * lasso_y + (1 - alpha) * ridge_y

plt.figure(figsize=(6,6))
plt.plot(elastic_x, elastic_y, label='Elastic Net', color='teal')
plt.plot(ridge_x, ridge_y, label='Ridge', color='black', linestyle='--')
plt.plot(lasso_x, lasso_y, label='Lasso', color='gray', linestyle=':')

plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

plt.xlabel(r'$\beta_1$')
plt.ylabel(r'$\beta_2$')
plt.title('Elastic net-Diagrammatic Representation')
plt.legend()
plt.grid(False)
plt.show()