import numpy as np
import pandas as pd

pokemon = pd.read_csv("pokemon_data.csv")
pokemon["Attack Ratio"] = pokemon["Attack"]/pokemon["Sp. Atk"]

poke = pokemon.set_index("Name")

print(poke.loc[["Bulbasaur", "Squirtle", "Charmander", "Arceus", "Vaporeon"]])

for index, row in poke.iterrows():
    print(index, " - ", row["Type 1"])