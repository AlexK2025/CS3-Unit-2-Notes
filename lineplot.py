import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.style.use("seaborn-v0_8-bright")

x = np.linspace(0, 10, 100)

fig = plt.figure()
ax = plt.axes()

plt.xlim(0, 10)
plt.ylim(-1, 1)

plt.plot(x, np.sin(x), "-c", label="sine")
plt.plot(x, np.cos(x), "-m", label="cosine")

plt.savefig("lineplot.png")