import sqlite3


sql_highest_avr_grade = """
SELECT ROUND(AVG(g.grade), 2) as gr, s.fullname
FROM grades as g
LEFT JOIN students as s ON g.student_id = s.id
GROUP BY s.id
ORDER BY gr DESC
LIMIT 5;
"""

sql_highest_avr_by_disc = """
SELECT aux_table.discipline, aux_table.student_name, MAX(aux_table.avg_grade) 
FROM (
  SELECT d.name as discipline, ROUND(AVG(grade), 2) as avg_grade, s.fullname as student_name
  FROM grades 
  LEFT JOIN students s ON s.id = grades.student_id 
  LEFT JOIN disciplines d ON d.id = grades.discipline_id 
  GROUP BY discipline_id, student_id
  ) as aux_table
GROUP BY aux_table.discipline;
"""

sql_avr_in_group_by_disc = """
SELECT aux_table.discipline, aux_table.group_name, ROUND(AVG(aux_table.avg_grade), 2) 
FROM (
  SELECT d.name as discipline, ROUND(AVG(grade), 2) as avg_grade, sg.name as group_name
  FROM grades 
  LEFT JOIN students s ON s.id = grades.student_id 
  LEFT JOIN disciplines d ON d.id = grades.discipline_id
  LEFT JOIN student_groups sg ON sg.id = s.group_id 
  GROUP BY discipline_id, sg.id
  ) as aux_table
GROUP BY aux_table.group_name, aux_table.discipline;
"""

sql_avr_among_all = """
SELECT ROUND(AVG(g.grade), 2) as gr
FROM grades as g;
"""

sql_disc_per_teacher = """
SELECT t.fullname, d.name 
FROM teachers t
LEFT JOIN disciplines d ON d.teacher_id = t.id;
"""

sql_students_in_groups = """
SELECT sg.name, s.fullname 
FROM student_groups sg
LEFT JOIN students s ON s.group_id = sg.id;
"""

sql_grades_in_groups_per_disc = """
SELECT d.name, sg.name, s.fullname, g.grade, g.received_on 
FROM grades g
LEFT JOIN students s ON s.id = g.student_id 
LEFT JOIN disciplines d ON d.id = g.discipline_id 
LEFT JOIN student_groups sg ON sg.id = s.group_id
WHERE sg.id = 1 and d.id = 1;
"""

sql_grades_in_group_on_the_last_lesson = """
SELECT d.name, sg.name, s.fullname, g.grade, g.received_on 
FROM grades g
LEFT JOIN students s ON s.id = g.student_id 
LEFT JOIN disciplines d ON d.id = g.discipline_id 
LEFT JOIN student_groups sg ON sg.id = s.group_id
WHERE sg.id = 1 AND d.id = 1 AND g.received_on = (
    SELECT g.received_on 
    FROM grades g
    LEFT JOIN students s ON s.id = g.student_id 
    LEFT JOIN student_groups sg ON sg.id = s.group_id
    WHERE g.discipline_id = 1 AND sg.id = 1
    ORDER BY g.received_on DESC
    LIMIT 1);
"""

sql_disciplines_per_student = """
SELECT s.fullname, d.name
FROM students s 
LEFT JOIN grades g ON g.student_id = s.id 
LEFT JOIN disciplines d ON d.id = g.discipline_id
GROUP BY s.fullname, d.name;
"""

sql_teacher_per_student = """
SELECT s.fullname, t.fullname, d.name  
FROM grades g 
LEFT JOIN students s ON s.id = g.student_id
LEFT JOIN disciplines d ON d.id = g.discipline_id   
LEFT JOIN teachers t ON t.id = d.teacher_id 
WHERE t.id = 1 AND g.student_id = 1
GROUP BY d.name;
"""

sql_avg_grade_per_teacher_for_student = """
SELECT t.fullname, s.fullname, ROUND(AVG(g.grade), 2) as avg_grade
FROM grades g 
LEFT JOIN students s ON s.id = g.student_id 
LEFT JOIN disciplines d ON d.id = g.discipline_id 
LEFT JOIN teachers t ON t.id = d.teacher_id 
WHERE t.id = 1 AND s.id = 1
GROUP BY s.fullname, t.fullname;
"""

sql_avg_grade_per_teacher = """
SELECT t.fullname, ROUND(AVG(g.grade), 2) as avg_grade
FROM grades g 
LEFT JOIN disciplines d ON d.id = g.discipline_id 
LEFT JOIN teachers t ON t.id = d.teacher_id 
WHERE t.id = 1
GROUP BY t.fullname;
"""


def execute_query(query, db):
    with sqlite3.connect(db) as conn:
        c = conn.cursor()
        c.execute(query)
        return c.fetchall()
