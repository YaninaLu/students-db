import sqlite3
from random import randint
from generate_data import get_grades_per_student, generate_data


DATABASE = "students.db"
GROUPS = [
    "СП-11",
    "СП-12",
    "СП-13"
]
DISCIPLINES = [
    "Фізкультура",
    "Математика",
    "Українська мова",
    "Хімія",
    "Фізика"
]


def insert_teachers(teachers_names, db):
    with sqlite3.connect(db) as conn:
        c = conn.cursor()
        sql_insert_teachers = """INSERT INTO teachers(fullname)
                                VALUES(?)"""
        c.executemany(sql_insert_teachers, zip(teachers_names))
        conn.commit()


def insert_disciplines(disciplines, db):
    teachers_ids = [randint(1, 3) for _ in range(len(disciplines))]
    with sqlite3.connect(db) as conn:
        c = conn.cursor()
        sql_insert_disciplines = """INSERT INTO disciplines(name, teacher_id)
                                    VALUES(?,?)"""
        c.executemany(sql_insert_disciplines, zip(disciplines, teachers_ids))
        conn.commit()


def insert_groups(group_names, db):
    with sqlite3.connect(db) as conn:
        c = conn.cursor()
        sql_insert_teachers = """INSERT INTO student_groups(name)
                                VALUES(?)"""
        c.executemany(sql_insert_teachers, zip(group_names))
        conn.commit()


def insert_students(students_names, db):
    group_ids = [1] * 10 + [2] * 10 + [3] * 10
    with sqlite3.connect(db) as conn:
        c = conn.cursor()
        sql_insert_disciplines = """INSERT INTO students(fullname, group_id)
                                        VALUES(?,?)"""
        c.executemany(sql_insert_disciplines, zip(students_names, group_ids))
        conn.commit()


def insert_grades(db):
    all_grades = []
    for student_id in range(1, 31):
        grades = get_grades_per_student(student_id)
        all_grades += grades

    with sqlite3.connect(db) as conn:
        c = conn.cursor()
        sql_insert_disciplines = """INSERT INTO grades(student_id, discipline_id, received_on, grade)
                                        VALUES(?,?,?,?)"""
        c.executemany(sql_insert_disciplines, all_grades)
        conn.commit()


def populate_db(db):
    students, teachers = generate_data()
    insert_teachers(teachers, db)
    insert_disciplines(DISCIPLINES, db)
    insert_groups(GROUPS, db)
    insert_students(students, db)
    insert_grades(db)
