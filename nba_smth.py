import pandas as pd

data = pd.read_csv("./gg/nba.csv", index_col="Name")

# print(data)

first = data.loc["Avery Bradley"]
second = data.loc["Jae Crowder"]

print(first, '\n' , second)