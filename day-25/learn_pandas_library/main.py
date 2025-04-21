# with open("weather_data.csv") as file:
#     list_data = file.readlines()
#     print(list_data)

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#             if row[1] != "temp":
#                 temperatures.append(int(row[1])) 

#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
temperatures = data["temp"].to_list()
# print(data["temp"].mean())
max = data["temp"].max()
# print(data[data["temp"] == max])

# avg = sum(temperatures)/len(temperatures)
# print(avg)

monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
monday_temp = (monday_temp * 1.8) + 32
print(monday_temp)

print("---------------")
print(type(monday))
