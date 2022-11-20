PRAGMA foreign_keys = off;
BEGIN TRANSACTION;
-- Table: students
DROP TABLE IF EXISTS students;
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname STRING UNIQUE NOT NULL,
    group_id REFERENCES student_groups (id)
);

-- Table: student groups
DROP TABLE IF EXISTS student_groups;
CREATE TABLE student_groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    name STRING UNIQUE
);

-- Table: disciplines
DROP TABLE IF EXISTS disciplines;
CREATE TABLE disciplines (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name STRING UNIQUE NOT NULL,
    teacher_id REFERENCES teachers (id)
);

-- Table: teachers
DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname STRING UNIQUE NOT NULL
);

-- Table: grades
DROP TABLE IF EXISTS grades;
CREATE TABLE grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id REFERENCES students (id),
    discipline_id REFERENCES disciplines (id),
    received_on DATE NOT NULL,
    grade INTEGER NOT NULL
);
COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
