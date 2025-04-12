#Pandas python library
# Panel Data -> 

import pandas as pd

# Series -> 1D array (one column in excel)
# DataFrame  -> 2D table (excel ko workbook , spreadsheet)

# data = {"name" : ["Sandesh", "Suman", "Buddhi", "Subash"], "Age": [15,20,25,30]}

# df = pd.DataFrame(data)
# print(df)

# Reading CSV file
df = pd.read_csv("data.csv")

#read excel file

# df = pd.read_excel("data.xlsx")

#to save in csv format.

# df.to_csv("outputsecond.csv", index=False) #it avoids extra column

# df= df.head()
# print(df)

# df = df.tail()
# df = df.shape # (row, column)
# print(df)

# print(df.info())

# print(df.describe())

# name = df[["name", "Age"]]
# print(name)

# firstRow = df.iloc[0]
# print(firstRow)

# ageGreaterTwenty = df[df["Age"]>20]

# print(ageGreaterTwenty)

# df.dropna()
# print(df.isnull())

# df.fillna(0)

# df["Salary"] = [2000,500,800,800,700,1000]
# print(df.head())

# df.drop("Salary", axis=1, inplace=True)
# print(df.head())

# seeThis = df.groupby("name") ["Salary"].mean()
# print(seeThis)

# df1 = pd.DataFrame({"ID":[1,2], "Name":["Sandesh", "Suman"]})
# df2 = pd.DataFrame({"ID":[1,2], "Salary":[10000,20000]})

# mergedTable = pd.merge(df1,df2, on = "ID")
# print(mergedTable)

df["date"] = pd.to_datetime(df["date"])
df.set_index("date", inplace=True)

print(df.head())


