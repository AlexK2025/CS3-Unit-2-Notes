import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

cities = pd.read_csv("california_cities.csv")

lat, lon = cities['latd'], cities['longd']
pop = cities['population_total']
area_water = cities['area_water_percent']

plt.axes().set_facecolor((0.074, 0.427, 0.082))
plt.scatter(lon, lat, c=np.log10(pop), cmap='YlOrBr', s=area_water, linewidth=0)

plt.axis('equal')
plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.colorbar(label='Population')
plt.clim(3, 7)

plt.title("Water Area and Population of California Cities")

plt.savefig("cali.png")