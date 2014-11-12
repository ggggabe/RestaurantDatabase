from __future__ import print_function
import pandas as pd

restaurants = pd.read_csv("Restaurants.csv")

with open("restaurant_names.csv", 'w+') as rn :
    for name in restaurants.Restaurant :
        print(name, file=rn)
