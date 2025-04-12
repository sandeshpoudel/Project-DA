import pandas as pd

#load cleaned data:
emails = pd.read_csv("./Day-7/cleanded.csv")

# print(emails.head())

#Load imdb scraped data
imdb = pd.read_csv("./imdb_top10.csv")
# print(imdb.head())

#merge emails to imdb titles
merged_df = imdb.copy()
# It creates a copy of the imdb DataFrame and assigns it to a new variable called merged_df.

# print(imdb.columns)

merged_df = pd.merge(imdb, emails, on='id', how='left')

merged_df.to_csv("merged_with_email.csv")
print("Successfully Completed.")
# print(merged_df.head())