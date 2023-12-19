import pandas as pd

# Read the data
data = pd.read_csv("intermediate/csv_work/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Get the counts of the squirrels which have different colors
grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

# Create a list that contains the counts of different colors of squirrels
counts = [grey_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]

# Create a dict to be able to create a DataFrame
data_dict = {
    "fur_color": ["grey", "red", "black"],
    "count": counts
}

new_data = pd.DataFrame(data_dict)
new_data.to_csv("intermediate/csv_work/different_color_squirrels_count.csv")
