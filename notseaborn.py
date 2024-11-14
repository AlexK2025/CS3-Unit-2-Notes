import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

#sns.set_style(style="ticks", palette="bright")

data = np.random.multivariate_normal([0, 0], [[5, 2], [2, 2]], size=2000)
data = pd.DataFrame(data, columns=['x', 'y'])

for col in 'xy':
    plt.hist(data[col], density=True, alpha=0.5)
plt.savefig("matplotlib.png")
plt.close()

sns.kdeplot(data=data, fill=True)
plt.savefig("kdeplot")
plt.close()

iris = sns.load_dataset("iris")
sns.pairplot(iris, hue="species", height=2.5)
plt.savefig("irispairplot.png",  bbox_inches="tight")
plt.close()

tips = sns.load_dataset('tips')
tips['tip_pct'] = 100 * tips['tip']/tips['total_bill']

grid = sns.FacetGrid(tips, row="sex", col="time", margin_titles=True)
grid.map(plt.hist, "tip_pct", bins=np.linspace(0, 40, 15))
plt.savefig("facetgrid.png")
plt.close()

g = sns.catplot(x="day", y="total_bill", hue="sex", data=tips, kind="box")
plt.savefig("catplot.png")
plt.close()

sns.jointplot(x="total_bill", y="tip", data=tips, kind="hex")
plt.savefig("jointplot.png")
plt.close()
