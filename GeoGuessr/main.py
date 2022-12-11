# method1
# # with open("weather_data.csv") as f:
# #     data = f.read()
# #     data = data.split("\n")
# # print(data)
# method 2
# import csv
# with open("weather_data.csv") as data_file:
#     data= csv.reader(data_file)
#     temperatures=[]
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)
#

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print(data["condition"])

data_dict = data.to_dict(orient="dict")
print(data_dict)
temp_list = data["temp"].to_list()
print(temp_list)
a = round(sum(temp_list) / len(temp_list), 2)
print(a)

avg=data["temp"].mean()
print(avg)
max = data["temp"].max()
print(max)

# Get data in row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]

print(int(monday.temp))
b=monday.temp*9/5+32
print(b)

data_dict = {
"students": ["Paul", "kaka", "TOm"],
"age": [12,32,55]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")