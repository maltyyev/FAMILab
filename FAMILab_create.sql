-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2015-10-12 13:20:22.857




-- tables
-- Table groups
CREATE TABLE groups (
    group_id int  NOT NULL,
    number int  NOT NULL,
    course int  NOT NULL,
    pulpit_id int  NOT NULL,
    CONSTRAINT groups_pk PRIMARY KEY (group_id)
);

-- Table pulpits
CREATE TABLE pulpits (
    pulpit_id int  NOT NULL,
    title varchar(50)  NOT NULL,
    description varchar(1000)  NOT NULL,
    CONSTRAINT pulpits_pk PRIMARY KEY (pulpit_id)
);

-- Table students
CREATE TABLE students (
    student_id int  NOT NULL,
    name varchar(40)  NOT NULL,
    phone int  NOT NULL,
    email varchar(40)  NOT NULL,
    group_id int  NOT NULL,
    CONSTRAINT students_pk PRIMARY KEY (student_id)
);

-- Table subjects
CREATE TABLE subjects (
    subject_id int  NOT NULL,
    title varchar(45)  NOT NULL,
    description varchar(1000)  NOT NULL,
    pulpit_id int  NOT NULL,
    CONSTRAINT subjects_pk PRIMARY KEY (subject_id)
);

-- Table subjects_by_teachers
CREATE TABLE subjects_by_teachers (
    subject_id int  NOT NULL,
    teacher_id int  NOT NULL,
    CONSTRAINT subjects_by_teachers_pk PRIMARY KEY (subject_id,teacher_id)
);

-- Table teachers
CREATE TABLE teachers (
    teacher_id int  NOT NULL,
    name varchar(40)  NOT NULL,
    biography varchar(1000)  NOT NULL,
    phone int  NOT NULL,
    email varchar(40)  NOT NULL,
    CONSTRAINT teachers_pk PRIMARY KEY (teacher_id)
);





-- foreign keys
-- Reference:  groups_pulpits (table: groups)


ALTER TABLE groups ADD CONSTRAINT groups_pulpits FOREIGN KEY groups_pulpits (pulpit_id)
    REFERENCES pulpits (pulpit_id);
-- Reference:  students_groups (table: students)


ALTER TABLE students ADD CONSTRAINT students_groups FOREIGN KEY students_groups (group_id)
    REFERENCES groups (group_id);
-- Reference:  subjects_by_teachers_subjects (table: subjects_by_teachers)


ALTER TABLE subjects_by_teachers ADD CONSTRAINT subjects_by_teachers_subjects FOREIGN KEY subjects_by_teachers_subjects (subject_id)
    REFERENCES subjects (subject_id);
-- Reference:  subjects_by_teachers_teachers (table: subjects_by_teachers)


ALTER TABLE subjects_by_teachers ADD CONSTRAINT subjects_by_teachers_teachers FOREIGN KEY subjects_by_teachers_teachers (teacher_id)
    REFERENCES teachers (teacher_id);
-- Reference:  subjects_pulpits (table: subjects)


ALTER TABLE subjects ADD CONSTRAINT subjects_pulpits FOREIGN KEY subjects_pulpits (pulpit_id)
    REFERENCES pulpits (pulpit_id);



-- End of file.

