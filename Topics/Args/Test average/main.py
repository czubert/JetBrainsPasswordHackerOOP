def average_mark(*args):
    sum_of_marks = 0
    number_of_students = 0
    for arg in args:
        sum_of_marks += arg
        number_of_students += 1
    return round(sum_of_marks / number_of_students, 1)
