import pandas


data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
color_data = data['Primary Fur Color'].value_counts()
color_data = color_data.reset_index()
color_data.columns = ['Fur color', 'Count']
color_data.to_csv('colors.csv')
