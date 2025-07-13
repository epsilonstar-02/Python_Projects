import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250712.csv")

color = pd.DataFrame(data=data["Primary Fur Color"].value_counts().reset_index())
print(color)
color.columns = ["Fur Color", "Count"]
color.to_csv("color.csv")