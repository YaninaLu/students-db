import faker
from random import randrange, randint
import datetime


NUMBER_OF_STUDENTS = 30
NUMBER_OF_TEACHERS = 3
START_OF_YEAR = datetime.date(2022, 9, 1)
END_OF_YEAR = datetime.date(2022, 12, 25)
NUMBER_OF_GRADES_PER_STUDENTS = 20
DISCIPLINES = [
    "Фізкультура",
    "Математика",
    "Українська мова",
    "Хімія",
    "Фізика"
]


def generate_names(num, fake_generator):
    res = []
    for _ in range(num):
        res.append(fake_generator.name())
    return res


def generate_data():
    fake_data_generator = faker.Faker('uk_UA')
    student_names = generate_names(NUMBER_OF_STUDENTS, fake_data_generator)
    teachers_names = generate_names(NUMBER_OF_TEACHERS, fake_data_generator)
    return student_names, teachers_names


def random_date(start, end):
    while True:
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)
        date = start + datetime.timedelta(seconds=random_second)
        if date.weekday() < 5:
            return date


def get_grades_per_student(student_id):
    res = []
    for disc in range(1, len(DISCIPLINES)+1):
        for grade in range(NUMBER_OF_GRADES_PER_STUDENTS//len(DISCIPLINES)):
            res.append((student_id, disc, random_date(START_OF_YEAR, END_OF_YEAR), randint(1, 100)))
    return res
