from app import app
import random
import os


@app.route('/')
def home():
   return "hello world!"

@app.route('/users')
def users():
   return {"first_name": "foo", "l_name": "bar"}


@app.route('/randomStudents')
def get_random_student():
   users_list = get_user_names()
   rand_user = random.choice(users_list)

   return {"random_user_name": rand_user}

@app.route('/randomStudentsUI')
def get_random_student_ui():
   rand_student = get_random_student()
   return f'<html><h1>{rand_student["random_user_name"]}</html>'


def get_user_names():
   #  students_path = "/Users/admas/Projects/teaching/QA-LIVE/qa-bootcamp-python-core/exercises/random_select_students/list_of_user_names.csv"
   #  students_path = "./data/list_of_user_names.csv"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    students_path = os.path.join(current_dir, '../data/list_of_user_names.csv')

    # my_file = open(students_path)
    # content = my_file.read()
    # my_file.close()

    with open(students_path, 'r') as f:
        content = f.readlines()

    clean_content = [i.strip() for i in content]
    # clean_content = []
    # for i in content:
    #     clean_content.append(i.strip())

    return clean_content



