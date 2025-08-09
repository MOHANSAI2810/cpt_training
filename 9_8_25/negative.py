import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'A': [1, 2, 3, 4, 5],
    'B': [10, 9, 7, 6, 5],
    'C': [2, 4, 6, 8, 10]
}

df = pd.DataFrame(data)
corr_matrix = df.corr()

pairs = []
for i in corr_matrix.columns:
    for j in corr_matrix.columns:
        if i < j and corr_matrix.loc[i, j] < 0:  # Only unique pairs and negative correlation
            pairs.append((i, j))

for x_var, y_var in pairs:
    plt.figure()
    plt.scatter(df[x_var], df[y_var])
    plt.title(f"Scatter plot of {x_var} vs {y_var} (corr={corr_matrix.loc[x_var, y_var]:.2f})")
    plt.xlabel(x_var)
    plt.ylabel(y_var)
    plt.show()
