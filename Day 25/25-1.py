# with open('weather_data.csv') as file:
#     data = file.readlines()
#     print(data)

# import csv
# with open('weather_data.csv') as file:
#     data = csv.reader(file)
#     temp = []
#     for row in data:
#         temp.append(row[1])
#         print(row)
#     temp.pop(0)
#     print(temp)

import pandas
data = pandas.read_csv('weather_data.csv')
# print(data['temp'])

data_dict = data.to_dict()
print(data_dict)

# temp_list = data['temp'].to_list()
# print(temp_list)
# print(data['temp'].mean())
# print(data['temp'].max())

# Get data in Columns
# print(data['condition'])
# print(data.condition)

# Get data in Row
# print(data[data.day == 'Monday'])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == 'Monday']
# print(monday.condition)
# monday_temp = int(monday.temp)
# monday_temp_f = monday_temp * 9/5 + 32
# print(monday_temp_f)

# Create a dataframe from scratch
# data_dict = {
#     'students': ['Amy', 'James', 'Angela'],
#     'scores': [76, 56, 65]
# }
# new_data = pandas.DataFrame(data_dict)
# new_data.to_csv('new_data.csv')
