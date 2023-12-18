import pandas as pd

# # Csv to dataframe
# data = pd.read_csv("intermediate/csv_work/weather_data.csv")

# # Dataframe to dictionary
# data_dict = data.to_dict()

# # Series to list
# temp_list = data["temp"].to_list()

# # Average temp
# data["temp"].mean() # = sum(temp_list) / len(temp_list)

# # Max temp
# data["temp"].max()

# # Get data in columns
# print(data["temp"])
# print(data.temp)

# # Get data in row, where the temp is max on that row
# print(data[data.temp == data.temp.max()])
# print("")

# monday_row = data[data.day == "Monday"]
# print(monday_row)
# print(monday_row["temp"])

# # Create Dataframe
# my_dict = {
#     "students": ["Amy", "James", "Jones"],
#     "Age": ["19", "18", "20"]
# }

# new_data = pd.DataFrame(my_dict)
# new_data.to_csv("intermediate/csv_work/my_csv.csv")

data = pd.read_csv("intermediate/csv_work/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

counts = [grey_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]

data_dict = {
    "fur_color": ["grey", "red", "black"],
    "count": counts
}

new_data = pd.DataFrame(data_dict)
new_data.to_csv("intermediate/csv_work/different_color_squirrels_count.csv")
