import pandas as pd
import numpy as np

data = pd.Series([0.25, 0.5, 0.75, 'hi'])
print(data)
grade = pd.Series(["freshmen", "sophomore", "junior", "senior"], index=[9, 10, 11, 12])
print(grade[9])

cookies_dict = {
    "double chocolate": 10,
    "chocolate chip": 8,
    "oatmeal raisin": 6,
    "snickerdoodle": 7,
    "dirt": 1
}

cookies = pd.Series(cookies_dict)

print("dirt rating: ", cookies["dirt"])