import numpy as np
from datetime import date
def  generating_student_data():
    # a student ID; 
    id_student = np.arange(1,11).reshape(-1,1)
    # a random birth date between 2000 and 2006
    np.random.seed(100)
    birth_date = np.random.randint(2000,2007,size=10).reshape(-1,1)
    # three random grades between 0 and 20;
    np.random.seed(100)
    grades = np.random.randint(21,size=(10,3)).reshape(-1,3)
    # the student's age; 
    current_year = date.today().year
    age = current_year - birth_date
    # vstack
    student = np.hstack([id_student,birth_date])
    student = np.hstack([student,grades])
    student = np.hstack([student,age])
    # the average of the three grades.
    average = np.average(student[:,2:5],axis = 1).reshape(-1,1)
    student = np.hstack([student,average])
    np.set_printoptions(suppress=True)
    return student
