import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.style.use("seaborn-v0_8-bright")

rng = np.random.default_rng(100)
data = rng.normal(size=1000)

plt.hist(data)
print("hi")

plt.savefig("histogram.png")