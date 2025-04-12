import pandas as pd

df = pd.read_csv("./data/netflix_titles.csv")

# print("----------------------------")
# print("-----Show Added in 2022-----")
# print("----------------------------")
# print(df[df["release_year"]==2021].shape[0])
# print(df[df["release_year"]==2021].agg({'title':'count'}))

# yearly_status = df.groupby('release_year').agg({'title':'count'})

# print("shows per year", yearly_status)

# Task 2: find average duration of movies by year
movie_only = df[df['type'] == 'Movie']

# Filter out rows that don't contain 'min' in duration
movie_only = movie_only[movie_only['duration'].str.contains('min', na=False)] #To exclude NaN values that would crash the analysis.

# Clean and convert
movie_only['duration'] = movie_only['duration'].str.replace('min', '').str.strip().astype(int)

# Group and aggregate
duration_stats = movie_only.groupby('release_year').agg({'duration':'mean'})
duration_stats.plot()
print('\nAVG movie duration (min):\n', duration_stats)
