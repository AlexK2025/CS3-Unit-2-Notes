import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.style.use("seaborn-v0_8-bright")


x = np.linspace(0, 10, 100)
y = np.cos(x)

plt.scatter(x, y, marker="o", color="gray")

plt.savefig("scatterplot.png")