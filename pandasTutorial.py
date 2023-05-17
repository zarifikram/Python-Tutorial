from ctypes.wintypes import HPALETTE
from unicodedata import name
import pandas as pd
import numpy as np
# df stands for dataframe
df = pd.read_csv("pokemon.csv")
# print(df)

# CRUD
# Create
# Read
# Update
# Delete

# Reading = Querying

# querying head and tails
# df.head(5)

# querying columns
# df.columns
# note : df.columns doesnt return numpy lists
# print(type(df.columns))

# querying different columns
# print(df[["name", "type1", "hp"]])

# querying different rows
# print(df.iloc[529 : 550])

# queuring rows using conditions
# print(df.loc[df["name"] == "Mewtwo"])


# query name and type 2 of all pokemons whose name start with "T"


# listOfNames = np.array(df["name"])

# print(df[df["name"].str.startswith("T")][["name", "type2"]])



# query name and height of all pokemons whose height is between 40 and 100

# print(df[(df["height_m"] >= .4) & (df["height_m"] <= 1)][["name", "height_m"]])


# query name hp and type 1 of all pokemons whose name contains 'k' and weight is less than 50 
# print(df[(df["name"].str.contains("k")) & (df["weight_kg"] < 50)][["name", "hp", "type1", "weight_kg"]])




# query name hp and type 1 of all pokemons whose name endsWith 'k' and weight is between than 19 and 100
# query name hp and type 1 of all legendary pokemons whose weight is more than 50  
# query name hp and type 1 of all pokemons whose name contains 'z', name is at least 6 characters long and hp is more than 50
# query name hp and type 1 of all fire type pokemons and hp is less than 100
# query name hp and type 1 of all fire type pokemons whose second type is electric

# describe()
# print(df.describe())

# nUnique()
# print(df["speed"].nunique())

# shape
# print(df.shape)

# sum()
# print(df.sum(axis=1))

# 'sp_attack', 'sp_defense', 'speed', 'hp', 'defense', 'attack',

# min max mean median var std count quantile 


# 'sp_attack', 'sp_defense', 'speed', 'hp', 'defense', 'attack'
# show me the name and stats of the most powerful pokemon
# print(df[df[['sp_attack', 'sp_defense', 'speed', 'hp', 'defense', 'attack']].sum(axis = 1) == df[['sp_attack', 'sp_defense', 'speed', 'hp', 'defense', 'attack']].sum(axis = 1).max()]["name"])
# show the name of the pokemon for which height and weight are null

# query the max hp of pokemons of each distinct type 1

print(df.groupby(by="type1")["hp"].max())


# query the total number of pokemons of each distnct type 1

