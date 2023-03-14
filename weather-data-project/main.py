# import csv

# with open("weather_data.csv", mode="r") as file:
#   data = csv.reader(file)
#   temperatures = []
#   for row in data:
#     if row[1] == 'temp':
#       pass
#     else:
#       temperatures.append(int(row[1]))

# print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")

data_dict = data.to_dict()

temp_list = data.temp.to_list()
temp_average = data.temp.mean()
temp_max = data.temp.max()

monday = data[data.day == "Monday"]

# monday_temp_c = monday.temp

monday_temp_f = float((monday.temp * (9/5)) + 32)

print(f"The average temp is {round(temp_average, 2)}")
print(f"The max temp is {round(temp_max, 2)}")
print(f"Monday's temp in F was {monday_temp_f}")
# print(data[data.temp == data.temp.max()])