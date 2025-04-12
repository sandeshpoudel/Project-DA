#I have two csv file which has

import pandas as pd

netflix = pd.read_csv(f"./data/netflix_titles.csv")

imdb = pd.read_csv(f"./data/IMDb--movide.csv")


# print(netflix.head())

# print(imdb.head())

netflix["title"] = netflix["title"].str.strip().str.lower()
imdb["title"] = imdb["title"].str.strip().str.lower()



mergedData = pd.merge(netflix, imdb, on = "title", how = "left")

print(mergedData.groupby('listed_in')['rating'].mean().sort_values(ascending=False))
# print(higestRating.head())