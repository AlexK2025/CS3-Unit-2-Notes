import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.style.use("seaborn-v0_8-bright")

rng = np.random.default_rng(1000)

mean = [0, 0]
cov = [[1,1], [1,2]]
x, y = rng.multivariate_normal(mean, cov, 100000000000000).T
plt.hexbin(x, y, gridsize=1000000)
cb  = plt.colorbar(label="count in bin")

plt.savefig("histogram.png")