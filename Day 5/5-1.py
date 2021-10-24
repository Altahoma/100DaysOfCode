# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
students = 0
total_height = 0
for height in student_heights:
    students += 1
    total_height += height
print(round(total_height / students))
