from random import randint


names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
students_score = {student: randint(1, 100) for student in names}
print(students_score)
passed_students = {student: score for student, score in students_score.items() if score > 60}
print(passed_students)
