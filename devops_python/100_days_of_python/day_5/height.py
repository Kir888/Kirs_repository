student_heights = [180, 124, 165, 173, 189, 169, 146]
total_height = 0
for n in student_heights:
    total_height = total_height + n
number_of_students = 0
for student in student_heights:
    number_of_students += 1
average_height = round(total_height/number_of_students)
print(average_height)

    