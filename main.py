from select import execute_query, sql_avg_grade_per_teacher, sql_highest_avr_grade, sql_highest_avr_by_disc, \
    sql_avr_among_all, sql_avr_in_group_by_disc, sql_disc_per_teacher, sql_students_in_groups, \
    sql_grades_in_groups_per_disc, sql_grades_in_group_on_the_last_lesson, sql_disciplines_per_student, \
    sql_teacher_per_student, sql_avg_grade_per_teacher_for_student
from populate_db import populate_db
from create_db import create_db


DATABASE = "students.db"
SCRIPT_FILE = "students.sql"


if __name__ == '__main__':
    create_db(SCRIPT_FILE, DATABASE)
    populate_db(DATABASE)
    print(f"Five students with the highest average grades: {execute_query(sql_highest_avr_grade, DATABASE)}")
    print(
        f"One student with the highest average grade per discipline: {execute_query(sql_highest_avr_by_disc, DATABASE)}")
    print(f"Average grade in group per discipline: {execute_query(sql_avr_in_group_by_disc, DATABASE)}")
    print(f"Average grade among all students: {execute_query(sql_avr_among_all, DATABASE)}")
    print(f"Teachers per discipline: {execute_query(sql_disc_per_teacher, DATABASE)}")
    print(f"List of students in groups: {execute_query(sql_students_in_groups, DATABASE)}")
    print(f"Grades in groups per discipline: {execute_query(sql_grades_in_groups_per_disc, DATABASE)}")
    print(
        f"Grades in groups per discipline on the last lesson: {execute_query(sql_grades_in_group_on_the_last_lesson, DATABASE)}")
    print(f"Disciplines that each student learns: {execute_query(sql_disciplines_per_student, DATABASE)}")
    print(f"Disciplines that a teacher teaches a student: {execute_query(sql_teacher_per_student, DATABASE)}")
    print(
        f"Average grade from a teacher to a particular student: {execute_query(sql_avg_grade_per_teacher_for_student, DATABASE)}")
    print(f"Average grade from a teacher: {execute_query(sql_avg_grade_per_teacher, DATABASE)}")
