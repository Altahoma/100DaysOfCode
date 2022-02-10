import pandas


student_dict = {
    'student': ['Angela', 'James', 'Lily'],
    'score': [56, 76, 98]
}

# Loop through a dict:
for key, value in student_dict.items():
    print(value)

print()
student_date_frame = pandas.DataFrame(student_dict)
print(student_date_frame)

# Loop though a data frame
print()
for key, value in student_date_frame.items():
    print(value)

# Loop though rows of a data frame
print()
for index, row in student_date_frame.iterrows():
    print(row)
