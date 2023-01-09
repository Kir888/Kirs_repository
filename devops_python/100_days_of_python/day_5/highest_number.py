student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
highest = 0
for n in student_scores:
    if n > highest:
        highest = n
print(f"The highest score in the class is {highest}")