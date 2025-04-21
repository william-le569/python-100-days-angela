# Task : Create a csv file to count number of squirrels.
# Fur Color, Count

import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Find the unique list
fur_color_list = data["Primary Fur Color"].dropna().to_list()
fur_color_unique_list = set(fur_color_list)

print(fur_color_unique_list)

# Create a dictionary

fur_color_dictionary = {}
for item in fur_color_list:
    if item is not None:
        fur_color_dictionary[item] = 0

print(fur_color_dictionary)

# for item in fur_color_list:
#     if item:
#         fur_color_dictionary[item] = data["Primary Fur Color"].str.count(item)
# fur_color_dictionary["Gray"] = data["Primary Fur Color"].str.count("Gray")
# print(fur_color_dictionary)

# for i in fur_color_unique_list:
#     for j in fur_color_list:
#         if j == i:
#             fur_color_dictionary[i] += 1

# print(fur_color_dictionary)

# # Create Dataframe and export csv

# fur_color_count = pd.DataFrame(fur_color_dictionary)

# print(fur_color_count)



# print(set(fur_color_list))

## ------- walk through

# import pandas as pd

# data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
# print(grey_squirrels_count)
# print(red_squirrels_count)
# print(black_squirrels_count)

# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
# }

# df = pd.DataFrame(data_dict)
# df.to_csv("squirrel_count.csv")