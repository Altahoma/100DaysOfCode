with open() as file:
    file1 = file.readlines()

with open('file2.txt') as file:
    file2 = file.readlines()

print(file1)
print(file2)

result = [int(num) for num in file1 if num in file2]

# for i in file1:
#     if i in file2:
#         result.append(int(i))
#
#
# for i in file1:
#     for j in file2:
#         if i == j:
#             result.append(int(i))

# Write your code above 👆
print(result)
