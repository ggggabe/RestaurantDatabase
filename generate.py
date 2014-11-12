import pandas as pd

restaurants = pd.read_csv("Restaurants.csv")
for name in restaurants.Restaurant :
    print name 
