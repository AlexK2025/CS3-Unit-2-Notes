import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import random

from sklearn.datasets import load_iris

plt.style.use("seaborn-v0_8-bright")

iris = load_iris()
features = iris.data.T
plt.scatter(features[0], features[1], s=100*features[3], c=iris.target, cmap="viridis")
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])

plt.savefig("scatterplot.png")