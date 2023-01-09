def print_student_names(**names):
    print(names["last_name"])
print_student_names(name="Yusuf", last_name="Turan")

#someone can call this kwargs
def empty_function():
    pass