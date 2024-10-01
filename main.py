import pandas as pd
import numpy as np

data = pd.Series([0.25, 0.5, 0.75, 'hi'])
grade = pd.Series(["freshmen", "sophomore", "junior", "senior"], index=[9, 10, 11, 12])

cookies_dict = {
    "double chocolate": 10,
    "chocolate chip": 8,
    "oatmeal raisin": 6,
    "snickerdoodle": 7,
    "dirt": 1
}

cookies = pd.Series(cookies_dict)

cookies_df = pd.DataFrame(cookies, columns=["rating"])

cookies_df["allergens"] = [True, True, True, True, False]

cookies_df["sweetness"] = {
    "double chocolate": 10,
    "chocolate chip":  9,
    "oatmeal raisin": 7,
    "snickerdoodle": 8,
    "dirt": -1,
    "dinosaur": 11
}


data = pd.Series(['a', 'c', 'e', 'g'], index=[1, 3, 5, 7])

print(data)

print(data.iloc[2:5])