print("Enter your first grade")
first_exam = 70
second_exam = 90
third_exam = 78

str = "First exam score is {}, third exam score is {}, third exam score is {}"

print(str.format(first_exam, second_exam, third_exam))

str = "First exam score is {2}, second exam score is {0}, third exam score {1}"

print(type(str.format(first_exam, second_exam, third_exam)))

