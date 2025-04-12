import pandas as pd

file = pd.read_csv("iris.csv")

# print(file.head())

# Filter rows where sepal_length > 5.
sepalGreaterThanFive = file[file["sepal_length"]>5]

# print(len(sepalGreaterThanFive))

mean_Petal_width = file.groupby("species") ["petal_width"].mean().reset_index()
# print(mean_Petal_width)

# file.to_csv("myresult.csv", index = False)

sepalGreaterThanFive.to_csv("greater5.csv", index=False)
mean_Petal_width.to_csv("mean.csv", index=False)