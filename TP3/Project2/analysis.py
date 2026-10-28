import numpy as np 
from students import generating_student_data

student_data = generating_student_data()


def mean_grades(student_data):
    return np.mean(student_data[:, 2:5], axis=1)

def median_grades(student_data):
    return np.median(student_data[:, 2:5], axis=1)

def std_grades(student_data):
    return np.std(student_data[:, 2:5], axis=1)
# max grade for each student
def max_grade(student_data):
    return np.max(student_data[:, 2:5], axis=1)
# min grade for each student
def min_grade(student_data):
    return np.min(student_data[:, 2:5], axis=1)
# max grade for all students
def max_grade_all(student_data):
    return np.max(student_data[:, 2:5])
# min grade for all students
def min_grade_all(student_data):
    return np.min(student_data[:, 2:5])

def max_average(student_data):
    return np.max(student_data[:, 6])

def min_average(student_data):
    return np.min(student_data[:, 6])

def mean_age(student_data):
    return np.mean(student_data[:, 5])

print(student_data)