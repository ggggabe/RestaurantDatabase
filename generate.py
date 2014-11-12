from __future__ import print_function
import pandas as pd
import argparse

'''
restaurants = pd.read_csv("Restaurants.csv")
with open("restaurant_names.csv", 'w+') as rn :
    for name in restaurants.Restaurant :
        print(name, file=rn)
'''

def sort_ingredients() : 
    type_array = ['meat','fish','nuts','veggies','fruits','misc','grains']
    with open("tables/Ingredient.csv", 'r') as rn :
        for item in rn : 
            print(item)
            user_input = int(raw_input("0 for meat, 1 for fish, 2 for nuts, 3 for veggies, 4 for fruits, 5 for misc, 6 for grains: "))
            with open('tables/' + type_array[user_input] + '.csv', 'a+') as f:
                print(item, file=f)

if __name__ == '__main__' :
    parser = argparse.ArgumentParser(description="deal with data") 
    parser.add_argument('-s','--sort_ingredients', action="store_true",help="sort the ingredients")
    args= parser.parse_args() 
    if args.sort_ingredients :
        sort_ingredients()
